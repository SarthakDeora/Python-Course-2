f = open("sarthak.txt", "w") # That "w" tells the computer that we are in write mode in the 
#file sarthak.txt but now anything we will write will replace everythihng in the file sarthak.txt 
f.write("This is what i wrote") # Now this .write function will write anything u want in it 
a = f.write("This is what i wrote")
print(a)
f.close() #Very important to close the file 
v = open("sarthak2.txt", "a") #  instead of replacing this will append the tex in the file
v.write("this is a line\n")
v.close()



# the function .write return the number of characters written to the file

#Now to read and append both at the same time u can use r+

l = open("sarthak2.txt", "r+")
print(l.read())
l.write("lol hai bhai lol hai \n")

