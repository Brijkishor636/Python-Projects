
file = open("Basics/text.txt", "r")
x = file.read()
print(x)

with open("Basics/text.txt", "a") as f:
    f.write("\nAnother file added")
    
newfile = open("Basics/text.txt", "r")
y = newfile.read()
print(y)

z = ["shyam", "satyam", "Prince"]
file = open("Basics/text.txt", "w")
for item in z:
    file.write(item + "\n")

file.close()

file = open("Basics/text.txt", "a")
file.write("Hi there\n")
file.close()

file = open("Basics/text.txt", "r")
c = file.read()
print(c)
file.close()
