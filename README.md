# Simulate-linux-files-and-directory-commands

A python program that can simulate linux files and directory commands such as list(ls) ,copy(cp) ,move(mv) ,rename(mv) ,delete(rm),file details(ls l), dirstr(directory structure) (without using any system command).

Run using: python sim.py

		Commands					Description	

B.1)	cd "dir"					Changes the current directory to "dir", if it exists.

B.2)	ls "dir"					Lists all the files and directories in "dir". Do not print files starting with “.” as terminal does. 

B.3)	ls -l -a  “dir”				Lists all the files and directories in "dir". But do print files starting with “.” as terminal does. 

B.4)	ls -al or ls -la			Lists all the files and directories in "dir". But do print files starting with “.” as terminal does. 

B.5) 	clear						Clears the screen as “clear” in terminal does.

B.6) 	rm -r	“top”				Recursively removes the directory rooted at “top”. Will also delete multiple directories if provided.
