from os import listdir, getcwd
from os.path import isfile, join

directory = getcwd()

def scanDir(toScan):
    scanned = listdir(toScan)
    dirs = [d for d in scanned if not isfile(join(toScan, d))]
    files = [d for d in scanned if isfile(join(toScan, d))]
    return dirs, files

if __name__ == "__main__":
    print(directory)
    dirs, files = scanDir(directory)
    for d in dirs:
        print "| " + d
    for f in files:
        print "L " + f
