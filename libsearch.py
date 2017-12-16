from __future__ import print_function
import sys
import os
import subprocess


class LibWalkerException(Exception): pass

def getcommandoutput(command):
    return subprocess.check_output(command, shell=True).decode("utf-8")

def main():
    basedir = sys.argv[1]
    if not os.path.exists(basedir): raise LibWalkerException("Path invalid")

    for rootdir, dirs, files in os.walk(basedir):
        for f in files:
            if f[-4:] == ".lib":
                print("Library {0}:". format(f))
                for line in filter(lambda x: x.find("vcrt_initialize") != -1, getcommandoutput("dumpbin /SYMBOLS {0}".format(f)).split("\n")): print("    {0}".format(line))

if __name__=="__main__":
    main()
