from os import listdir, getcwd
from os.path import isfile, join, dirname

from colorama import Fore, Style

directory = getcwd()

def scanDir(toScan):
    scanned = listdir(toScan)
    dirs = []
    files = []
    for n in scanned:
        if isfile(join(toScan, n)):
            files.append(n)
        else:
            dirs.append(n)
    return dirs, files

def printf(filename, level):
    text = ""
    for i in range(level):
        text += "|"
    text += "L" + Fore.BLUE + filename + Style.RESET_ALL
    print(text)

def printd(dirname, level):
    text = ""
    for i in range(level + 1):
        text += "|"
    text += Fore.GREEN + dirname + Style.RESET_ALL
    print(text)

if __name__ == "__main__":
    splitDir = directory.split("/")
    print(splitDir[len(splitDir)-1])

    dirs, files = scanDir(directory)
    for d in dirs:
        printd(d, 0)
        
        # Prueba de segundo nivel (a automatizar)
        subdirs, subfiles = scanDir(join(directory, d))
        for dd in subdirs:
            printd(dd, 1)
        for ff in subfiles:
            printf(ff, 1)  

    for f in files:
        printf(f, 0)
