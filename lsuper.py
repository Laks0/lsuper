import sys

from os import listdir, getcwd
from os.path import isfile, join, dirname

from colorama import Fore, Style, Back

directory = getcwd()

depth = 0
if len(sys.argv) > 1:
    depth = int(sys.argv[1])

def scanDir(toScan):
    scanned = listdir(toScan)
    dirs = []
    files = []
    for n in scanned:
        if isfile(join(toScan, n)):
            files.append(n)
        else:
            dirs.append(n)
    dirs.sort()
    files.sort()
    return dirs, files

def printf(filename, level):
    text = ""
    for i in range(level):
        text += "|"
    text += "L"
    text += Back.BLACK * (filename[0] == ".") + Fore.BLUE
    text += filename
    text += Style.RESET_ALL
    print(text)

def printd(dirname, level):
    text = ""
    for i in range(level + 1):
        text += "|"
    text += Back.BLACK * (dirname[0] == ".") + Fore.GREEN
    text += dirname
    text += Style.RESET_ALL
    print(text)

def printFullDir(path, layer):
    dirs, files = scanDir(path)
    for d in dirs:
        printd(d, layer)
        if layer < depth:
            printFullDir(join(path, d), layer + 1)
    for f in files:
        printf(f, layer)

def main():
    splitDir = directory.split("/")
    print(Fore.RED + splitDir[len(splitDir)-1] + Style.RESET_ALL)

    printFullDir(directory, 0)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h":
            print("lsuper [DEPTH = 0]")
        else:
            main()
    else:
        main()
