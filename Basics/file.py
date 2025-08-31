import os


if os.path.exists("Basics/text.txt"):
    os.remove("Basics/text.txt")
else: 
    print("File doesn't exists in this folder")

