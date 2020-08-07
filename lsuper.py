import sys

from os import listdir, getcwd
from os.path import isfile, join, getsize

from colorama import Fore, Style, Back

#from humanize import naturalsize
from human import human

directory = getcwd()

depth = 0
showHidden = True
onlyFiles = False
onlyDirs = False
minimal = False
byts = False
binary = False

infoSpace = 40

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

    text += Back.BLACK * (filename[0] == ".") + Fore.BLUE

    text += filename
    outputLen += len(filename)

    text += Style.RESET_ALL
    if minimal:
        print(text)
        return

    for i in range(infoSpace - outputLen): 
        text += " "
    text += "|"
    
    size = getsize(join(path, filename))
    if byts:
        text += str(size)
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
    print("lsuper [-h help] [-d <depth> (0)] [-m minimal] [-b bytes] [-i binary] [--noHidden] [--onlyFiles] [--onlyDirs]")

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
            elif arg == "-b":
                byts = True
            elif arg == "-h":
                printHelp()
                execute = False
                break
        if execute:
            main()
    else:
        main()
