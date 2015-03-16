# Simulate-linux-files-and-directory-commands

A python program that can simulate linux files and directory commands such as list(ls) ,copy(cp) ,move(mv) ,rename(mv) ,delete(rm),file details(ls l), dirstr(directory structure) (without using any system command).

Run using: python sim.py

	Commands		Description	

B.1) cd "dir"			Changes the current directory to "dir", if it exists.

B.2) ls "dir" {-l, -a, -h}	Lists all the files and directories in "dir". 

B.5) clear			Clears the screen as “clear” in terminal does.

B.6) rm “top” {-i, -r}		Recursively removes the directory rooted at “top”. Will also delete multiple directories if provided.

B.7) dirstr 			Print the directory structure of the current directory in heirarchial format.

B.8) cp	{-r}			copy

B.9) cd				change directory

B.10)mv or rename {-r}		moves or rename
