
import sys
from os import system


def concatenate(first, last):
    command = "pdftk "
    for i in range(first, last+1):
        command = command + " book"+str(i)+".pdf"
    command = command + " cat output recopilation-Books"+str(first)+"To"+str(last)+".pdf"

    print command
    system(command)


first = int(sys.argv[1])
last = int(sys.argv[2])
concatenate(first,last)
