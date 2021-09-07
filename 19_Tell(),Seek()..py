f = open("sarthak2.txt")
print(f.tell())  #This function tells that where is the current position of the computer in the file.
print(f.readline()) #This prints a line of a file.
print(f.tell())
f.seek(0) # this brngs the computer at the character in the bracket file
print(f.readline()) #This prints a line of a file
f.close()