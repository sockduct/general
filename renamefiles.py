# Imports
import os
import re

# Variables
# For Windows use a raw string since backslashes are used
# e.g., dirpath = r'c:\users\george\documents\reference\analysts\Example'
dirpath = r'<drive>:\Users\<username>\Documents\Reference\Analysts\<analyst>'
#filererm = r'\D'
filererm = r'<analyst>-'

# Rename files use regexp
def renamefilesre():
    dirfiles = os.listdir(dirpath)
    for dirfile in dirfiles:
        newfile = re.findall(filererm,dirfile)
        newfile = ''.join(newfile)
        #os.rename(dirfile,newfile)
        print "Old filename:  " + str(dirfile)
        print "New filename:  " + str(newfile)

# Rename files using string translation
def renamefilessttr():
    count = 0
    dirfiles = os.listdir(dirpath)
    savedir = os.getcwd()
    os.chdir(dirpath)
    for dirfile in dirfiles:
        newfile = dirfile.translate(None,"0123456789")
        print("Old filename:  " + dirfile)
        print("New filename:  " + newfile)
        os.rename(dirfile,newfile)
        count += 1
    os.chdir(savedir)
    print("\nRenamed " + str(count) + " files.\n")

# Rename files using string replace
def renamefilesstrp():
    count = 0
    dirfiles = os.listdir(dirpath)
    savedir = os.getcwd()
    os.chdir(dirpath)
    for dirfile in dirfiles:
        newfile = dirfile.replace(filererm,'',1)
        print("Old filename:  " + dirfile)
        print("New filename:  " + newfile)
        os.rename(dirfile,newfile)
        count += 1
    os.chdir(savedir)
    print("\nRenamed " + str(count) + " files.\n")

#renamefilesre()
#renamefilessttr()
renamefilesstrp()

