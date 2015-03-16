import os,sys,getpass,shutil,commands

BLUE = 4

def my_print(text,colour):
                sequence = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
		p = sys.stdout                
		p.write(sequence)

def extract_(s):
	s = s.split()
	files = []
	args = []
	cmd = s[0]
	directory = []
	if cmd=="mv" or cmd=="rename":
		for i in range(1,len(s)):	
			try:		
				if s[i][0]=='-':
					args.append(s[i])
				elif os.path.isfile(s[i]):
					files.append(s[i])
				elif os.path.exists(os.getcwd()+"/"+s[i]): 
					directory.append(os.getcwd()+"/"+s[i])
				elif os.path.exists(os.path.split(s[i])[1]):
					directory.append(os.getcwd()+"/"+os.path.split(s[i])[1])
				elif os.path.exists(s[i]): 
					directory.append(s[i])
				else:
					directory.append(s[i])
			
			except (OSError,IOError):
				print "cannot access "+s[i]+": No such file or directory"
				return -1
		return (cmd,args,directory,files)

			
	for i in range(1,len(s)):	
		try:		
			if s[i][0]=='-':
				args.append(s[i])
			elif os.path.isfile(s[i]):
				files.append(s[i])
			elif os.path.exists(os.getcwd()+"/"+s[i]): 
				directory.append(os.getcwd()+"/"+s[i])
			elif os.path.exists(os.path.split(s[i])[1]):
				directory.append(os.getcwd()+"/"+os.path.split(s[i])[1])
			elif os.path.exists(s[i]): 
				directory.append(s[i])			
			else:
				print "cannot access \'"+s[i]+"\': No such file or directory"
				return -1
			
		except (IOError,OSError):
			print "cannot access "+s[i]+": No such file or directory"
			return -1
	return (cmd,args,directory,files)

def cd(directory):
	try:	
		if len(directory) == 0:
			return -1	
		else:
			os.chdir(directory[0])
	except (OSError,IOError):
		print "cannot access \'"+s[i]+"\': No such file or directory"

def ls(args,directory):
	argument_count=len(args)
	dirs = os.listdir(os.getcwd())
	if argument_count==0:
		 if len(directory) == 0:
			for files in dirs:
				if files[0]!='.' and os.path.isfile(files):
					print files+"\t",
					print ""				
				elif files[0]!=".":
					my_print(files + "\t",BLUE)
					print ""

		 elif len(directory) == 1:
			os.chdir(directory[0])
			dirs = os.listdir(os.getcwd())
			for files in dirs:
				if files[0]!='.' and os.path.isfile(files):
					print files + "\t",
					print ""
				elif files[0]!=".":
					my_print(files + "\t",BLUE)
					print ""


	elif argument_count==1:
		if len(directory) == 0:
			if args[0]=='-l':
				for files in dirs:
					if os.path.isfile(files) and files[0]!=".":
						print commands.getstatus(files),
					else:
						my_print(commands.getstatus(files),BLUE)
					print ""

			elif args[0]=='-a':
				for files in dirs:
					if os.path.isfile(files) and files[0]!=".":
						print files + "\t",
					else:
						my_print(files + "\t",BLUE)
					print ""
			
			elif args[0]=="-la" or args[0]=="-al":
				if len(directory) == 0:
					for files in dirs:
						if os.path.isfile(files):
							print commands.getstatus(files),
						else:
							my_print(commands.getstatus(files),BLUE)
						print ""
			
				else:
					print "enter single directory only"

			else:
				print "No such option"
		
		elif len(directory) == 1:
			os.chdir(directory[0])
			dirs = os.listdir(os.getcwd())
			if args[0]=='-l':
				for files in dirs:
					if os.path.isfile(files) and files[0]!=".":
						print commands.getstatus(files),
					else:
						my_print(commands.getstatus(files),BLUE)
					print ""
			elif args[0]=='-a':
				for files in dirs:
					if os.path.isfile(files):
						print files + "\t",
					else:
						my_print(files + "\t",BLUE)
					print ""

			elif args[0]=="-la" or args[0]=="-al":
				os.chdir(directory[0])
				dirs = os.listdir(os.getcwd())
				for files in dirs:
					if os.path.isfile(files):
						print commands.getstatus(files),
					else:
						my_print(commands.getstatus(files),BLUE)
					print ""
			
				else:
					print "enter single directory only"
			else:
				print "No such option"
	
	elif argument_count==2:
		if (args[0]=="-l" and args[1]=="-a") or (args[0]=="-a" and args[1]=="-l"):
			if len(directory) == 0:
				for files in dirs:
					if os.path.isfile(files):
						print commands.getstatus(files),
					else:
						my_print(commands.getstatus(files),BLUE)
					print ""
			elif len(directory) == 1:
				os.chdir(directory[0])
				dirs = os.listdir(os.getcwd())
				for files in dirs:
					if os.path.isfile(files):
						print commands.getstatus(files),
					else:
						my_print(commands.getstatus(files),BLUE)
					print ""
			
			else:
				print "enter single directory only"
	else:
		print "More than 2 arguments are not allowed."

def clear():
	sys.stderr.write("\x1b[2J\x1b[H")	

def remove(args,directory,files):
	try:
		count_arguments = len(args)
		count_files = len(files)
		if count_arguments==0:
			if count_files==0 and len(directory) == 0:
				print "rm: missing operand"
			elif count_files!=0 and len(directory) == 0:
				for i in files:
					os.remove(i)
			elif count_files==0 and len(directory) != 0:
				for i in range(0,len(directory)):
					print "rm: cannot remove \'"+directory[i]+"\': Is a directory"
			elif count_files!=0 and len(directory) != 0:
				for i in files:
					os.remove(i)
				for i in range(0,len(directory)):
					print "rm: cannot remove \'"+directory[i]+"\': Is a directory"
	
		elif count_arguments==1:
			if args[0]=="-r":
				if count_files==0 and len(directory) == 0:
					print "rm: missing operand"
				elif count_files!=0 and len(directory) == 0:
					for i in files:
						os.remove(i)
				elif count_files==0 and len(directory) != 0:
					for i in directory:
						for root, dirs, files in os.walk(i, topdown=False):
	    						for name in files:
								os.remove(os.path.join(root, name))
	    						for name in dirs:
								os.rmdir(os.path.join(root, name))
						os.removedirs(i)
				elif count_files!=0 and len(directory) != 0:
					for i in files:
						os.remove(i)
					for i in directory:
						for root, dirs, files in os.walk(i, topdown=False):
	    						for name in files:
								os.remove(os.path.join(root, name))
	    						for name in dirs:
								os.rmdir(os.path.join(root, name))
						os.removedirs(i)					

			elif ("-i" in args):
				print "Do you really want to delete:(Y/N)",
				r = raw_input()
				r = r.lower()
				if r=="y":
					args=[]
					remove(args,directory,files)
				else:
					return

			elif ("-ri" in args or "-ir" in args):
				print "Do you really want to delete:(Y/N)",
				r = raw_input()
				r = r.lower()
				if r=="y":
					args=["-r"]
					remove(args,directory,files)
				else:
					return
		
			else:
				print "rm: invalid option --\'"+args[0]+"\'"
			
		elif count_arguments==2:
			if (args[0]=="-i" and args[1]=="-r") or (args[0]=="-r" or args[1]=="-i"):
				print "Do you really want to delete:(Y/N)",
				r = raw_input()
				r = r.lower()
				if r=="y":
					args=["-r"]
					remove(args,directory,files)
				else:
					return
			else:
				print "Arguments other than -i and -r are not avaialble."
			
		else:
			print "Multi argument option not available."
	except(OSError,IOError):
		print "Remove Error."

def copy(args,files,directory):
	try:
		if len(args)==0:
			if len(files)==1 and len(directory)==1:
				if os.path.isfile(directory[0]+"/"+files[0]):
					os.remove(directory[0]+"/"+files[0])
				shutil.copy(files[0],directory[0])
			elif len(directory)==2:
				print "cp: omitting directory \'"+directory[0]+"\'"
			else:
				print "Invalid option"

		elif len(args)==1:
			
			if len(files)==0 and len(directory)==2 and args[0]=="-r":
				if os.path.isdir(directory[1]+"/"+os.path.split(directory[0])[1]):
					for root, dirs, files in os.walk(directory[1]+"/"+os.path.split(directory[0])[1], topdown=False):
    						for name in files:
        						os.remove(os.path.join(root, name))
    						for name in dirs:
       							os.rmdir(os.path.join(root, name))
					os.rmdir(directory[1]+"/"+os.path.split(directory[0])[1])
					shutil.copytree(directory[0],directory[1])

				elif os.path.isdir(directory[1]):
					shutil.copytree(directory[0],directory[1]+"/tarung")
					os.rename(directory[1]+"/tarung",directory[1]+"/"+os.path.split(directory[0])[1])
						
			else:
				print "Not a valid option."

		else:
			print "Single argument allowed only"

	except(OSError,IOError):
		print "Overwrite not allowed."

def dirstr(directory,dep):
	try:
		depth = dep
		for files in os.listdir(directory):
			if os.path.isdir(directory+"/"+files)==True:
				print " "+"| "*(depth+1)
				print (" "+"| "*(depth)+"#---------------  Folder Name: "+files+"/ ---------------#")
				dirstr(directory+"/"+files,depth+1)
		if os.listdir(directory) == []:
			print "\n                   (EMPTY FOLDER)                             "
		else:
			for files in os.listdir(directory):
				if os.path.isdir(directory+"/"+files)==False:
					print " "+"| "*(depth+1)
					print (" "+"| "*(depth)+"#-")+files
			return
	except(OSError,IOError):
		print "dirstr Error."

def move(files,directory):
	try:
		if len(files)==1 and len(directory)==1:
			if os.path.isfile(directory[0]+"/"+files[0]):
				os.remove(directory[0]+"/"+files[0])
			shutil.move(files[0],directory[0])
		elif len(files)==0 and len(directory)==2:
			if os.path.isdir(directory[1]+"/"+os.path.split(directory[0])[1]):
				for root, dirs, files in os.walk(directory[1]+"/"+os.path.split(directory[0])[1], topdown=False):
    					for name in files:
        					os.remove(os.path.join(root, name))
    					for name in dirs:
       						os.rmdir(os.path.join(root, name))
				os.rmdir(directory[1]+"/"+os.path.split(directory[0])[1])
			shutil.move(directory[0],directory[1])
		else:
			print "Not valid."
			return

	except (IOError,OSError):
		print "Move Error"

def main():
	
	pwd = os.getcwd()
	while(True):	
		os.chdir(pwd)
		print getpass.getuser()+"@shell~: "+pwd+"$ ",
		s = raw_input()

		if s.isspace() or s=="":
			continue		
		args = []
		files = []
		directory = []
		if(extract_(s)!=-1):
			cmd, args, directory, files = extract_(s)
		else:
			continue

		if cmd=="":
			continue
		elif s=='exit' or s=='quit':
			return	
		elif cmd=="ls":
			ls(args,directory)
		elif cmd=="cd":
			cd(directory)
			pwd = os.getcwd()
		elif cmd=="clear":
			clear()
		elif cmd=="rm":
			remove(args,directory,files)
		elif cmd=="cp":
			copy(args,files,directory)		
		elif cmd=="mv" or cmd=="rename":
			move(files,directory)
		elif cmd=="dirstr":
			print ("#---------------  Folder Name: "+os.path.split(os.getcwd())[1]+"/ ---------------#")
			dirstr(os.getcwd(),1)	
		else:
			print "No command \'"+cmd+"\' found"	

if __name__ == "__main__":
	main() 

