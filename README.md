# keyboards

Supporting simulated annealing code for the [Why I Made The World's Worst Keyboard](https://youtu.be/188fipF-i5I) YouTube video.

Written in Julia... because it's fast, easy to read, and annoys my labmates.

To run, download both filtes to the same directory and execute the Julia code. It should start by benchmarking your training data (myBook.txt) against QWERTY followed by building it's own optimal layout. Change the number of iterations and cooling rates as desired within the SA() function. The terminal will give some indication of current progres (also stored by a new text file will give a iteration-by-iteration record of progress), and .png files of the current best solution will be saved to your same directory.

To train on your own custom dataset either point the "myBook.txt" somewhere else or just replace its contents.

Good luck!

# My Additions
getFiles.py gets all the files in a specified directory (and all subdirectories excluding some select directory names) and reads the files. All the plaintext in these files is appended to code.txt. You can run the script on this file to analyze your documents and find your optimal keyboard.

`allowed_extensions` on line 19 and `dirs` on line 30 in `getFiles.py` should be changed to cater for your programming habits/system files