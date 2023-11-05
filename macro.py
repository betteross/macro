import os
import sys
import shutil

try:
    sys.argv[1]
except IndexError:
    print("Usage: macro <file>")

print("Welcome To The Macro Text Editor")
file = open(sys.argv[1], "w")
while True:
    text = input(": ")
    if text == "^X":
        break
    else:
        file.write(text)
      
