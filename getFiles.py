import os
import requests
from requests.auth import HTTPBasicAuth
from configparser import ConfigParser
import json

# Read configuration from config.ini
config = ConfigParser()
config.read('config.ini')

# Get GitHub credentials from the configuration
DIRECTORY = config.get('INPUT', 'dir')
FILE_OUT = config.get('OUTPUT', 'fileName')
outfile = open(FILE_OUT, "w")

print(f"Searching: {DIRECTORY}")

# Specify the file extensions you want to download
allowed_extensions = ['.py', '.java', '.asm', '.hs', '.tex', '.ino', '.pde', '.md']

dir_no = 0
def collect_files(directory, allowed_extensions=None):
    global dir_no
    dir_no += 1
    if (dir_no % 200 == 0):
        print(f"Dir {dir_no}, {directory}")
    all_files = set()

    for root, dirs, files in os.walk(directory):
        # Exclude directories with specified names
        dirs[:] = [d for d in dirs if d.lower() not in {'ardour', '.vs', 'cpp', 'javadoc', '.git', 'lib', 'libs', 'include', 'bin', 'out', 'docs', 'examples', 'library', 'libraries', 'env', 'venv', 'cmake-build-debug'}]

        # Append files with the correct extensions
        for file in files:
            if allowed_extensions and any(file.endswith(ext) for ext in allowed_extensions):
                file_path = os.path.join(root, file)
                all_files.add(file_path)

        # Recursively call the function for each subdirectory
        for subdir in dirs:
            subdir_path = os.path.join(root, subdir)
            all_files.update(collect_files(subdir_path, allowed_extensions))

    return all_files

all_files = collect_files(DIRECTORY, allowed_extensions)

print(f"Found: {len(all_files)} files")
for f in all_files:
    if any(f.endswith(ext) for ext in allowed_extensions):
        with open(f, 'r') as file:
            try:
                lines = file.readlines()
                outfile.writelines(lines)
            except Exception as e:
                print(f"Cannot parse file {file}")
            

outfile.close()
print("Download complete.")
