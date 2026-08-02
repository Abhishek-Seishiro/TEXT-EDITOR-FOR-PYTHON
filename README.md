# Simple Text Editor (Python)

This is a basic text editor I built using Python that runs in the terminal. It lets you write text, view it, save it to a file, open an existing file, clear the text, and count the total words — all through a simple menu.

I made this project as a beginner to practice working with file handling in Python (reading and writing files) along with loops and conditionals.

## What it does

- Write text into the editor (type DONE on a new line to finish)
- View the text currently in the editor
- Save the text to a .txt file
- Open an existing .txt file and load its content into the editor
- Clear the text (with a yes/no confirmation before deleting)
- Count the total number of words in the current text
- Exit the program

## What I learned / used

- Python basics (loops, if-elif-else, input/output)
- File handling - opening, reading, and writing files using open()
- try-except blocks to handle errors (like trying to open a file that doesn't exist)
- Splitting text into words using .split()
- Using a while True loop to keep a menu running until the user exits

## How to run it

python pjt3.py

## Things I want to improve later

- Fix a bug where choosing View Text or Count Words before writing anything can cause an error
- Add an option to append to a file instead of always overwriting it
- Add undo/redo support
- Turn this into a GUI text editor using Tkinter

## Made by

Abhishek Seishiro
