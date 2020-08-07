import sys

from os import listdir, getcwd
from os.path import isfile, join

from colorama import Fore, Style, Back

directory = getcwd()

depth = 0
showHidden = True
onlyFiles = False
onlyDirs = False

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
        if d[0] == "." and not showHidden:
            continue

        if not onlyFiles:
            printd(d, layer)

        if layer < depth:
            printFullDir(join(path, d), layer + 1)

    if not onlyDirs:
        for f in files:
            if f[0] == "." and not showHidden:
                continue
            printf(f, layer)

def main():
    splitDir = directory.split("/")
    print(Fore.RED + splitDir[len(splitDir)-1] + Style.RESET_ALL)

    printFullDir(directory, 0)

def printHelp():
    print("lsuper [-h help] [--noHidden] [--onlyFiles] [--onlyDirs] [-d <depth> (0)]")

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
            elif arg == "-h":
                printHelp()
                execute = False
                break
        if execute:
            main()
    else:
        main()
