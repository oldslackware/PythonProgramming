#!/usr/bin/python

def printAllFile(myfile):
    print("Read all file")
    print(myfile.read())
    "Return the position of reading at the start of file"
    myfile.seek(0)

def printForLine(myfile):
    print("\nUse of readline\n")
    print(myfile.readline())
    "Use readlines to read all lines with separator"
    myfile.seek(0)

def printInPos(myfile,pos):
    print("\nUse of readlines\n")
    print(myfile.readlines()[pos])
    myfile.seek(0)

def printLineByLine(file):
    for videogame in videogames_file.readlines():
        print(videogame)

videogames_file=open("videogames.txt" , "r")
"r => reading w => writing a => append or r+ => reading and writing"
if(videogames_file.readable()):
    print("\nYou can read the file\n")
    printAllFile(videogames_file)
    printForLine(videogames_file)
    printInPos(videogames_file, 5)
    print("\nThe right way to prin all lines\n")
    printLineByLine(videogames_file)
else:
    print("You can not read the file")

videogames_file.close()
print("-"*20)
print("File close")
print("-"*20)


