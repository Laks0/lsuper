import sys

from os import listdir, getcwd
from os.path import isfile, join, getsize

from colorama import Fore, Style, Back

from human import human
from config import *

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
    dirs.sort()
    files.sort()
    return dirs, files

def printf(filename, level, path):
    outputLen = 0
    text = ""

    for i in range(level):
        text += "|"
        outputLen += 1

    text += "L"
    outputLen += 1

    # Colors
    text += Back.BLACK * (filename[0] == ".") + Fore.BLUE

    text += filename
    outputLen += len(filename)

    text += Style.RESET_ALL
    if minimal:
        print(text)
        return

    ### INFOBAR ###
    for i in range(infoSpace - outputLen): 
        text += " "
    text += "|"
    
    # Size
    size = getsize(join(path, filename))
    if force:
        text += "%.1f" % (size/factor)
    else:
        text += human(size, binary)

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
        if d[0] == "." and not showHidden:
            continue

        if not onlyFiles:
            printd(d, layer)

        if layer < depth:
            printFullDir(join(path, d), layer + 1)

    if onlyDirs:
        return
    
    for f in files:
        if f[0] == "." and not showHidden:
            continue
        printf(f, layer, path)

def main():
    splitDir = directory.split("/")
    print(Fore.RED + splitDir[len(splitDir)-1] + Style.RESET_ALL)

    printFullDir(directory, 0)

def printHelp():
    print("lsuper [-h help] [-d <depth> (0)] [-m minimal] [-f force unit to default] [-fd <name> (b) force unit to one in the dictionary] [-fc <factor> (1) force unit to a specific factor] [-i binary] [--noHidden] [--onlyFiles] [--onlyDirs]")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        execute = True
        for i, arg in enumerate(sys.argv):
            if i == 0:
                continue
            if arg == "-d":
                depth = int(sys.argv[i+1])
            elif arg == "--onlyFiles":
                onlyFiles = True
            elif arg == "--onlyDirs":
                onlyDirs = True
            elif arg == "--noHidden":
                showHidden = False
            elif arg == "-m":
                minimal = True
            elif arg == "-i":
                binary = True
            elif arg == "-f":
                force = True
            elif arg == "-fd":
                force = True
                factor = units[sys.argv[i+1]]
            elif arg == "-fc":
                force = True
                factor = float(sys.argv[i+1])
            elif arg == "-h":
                printHelp()
                execute = False
                break
        if execute:
            main()
    else:
        main()
