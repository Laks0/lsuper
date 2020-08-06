from os import listdir, getcwd
from os.path import isfile, join

from colorama import Fore, Style

directory = getcwd()

def scanDir(toScan):
    scanned = listdir(toScan)
#    dirs = [d for d in scanned if not isfile(join(toScan, d))]
#    files = [d for d in scanned if isfile(join(toScan, d))]
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

if __name__ == "__main__":
    print(directory)
    dirs, files = scanDir(directory)
    for d in dirs:
        print( "| " + d)
        
        # Prueba de segundo nivel (a automatizar)
        subdirs, subfiles = scanDir(join(directory, d))
        for dd in subdirs:
            print ("|| " + dd)
        for ff in subfiles:
            printf(ff, 1)  

    for f in files:
        printf(f, 0)
