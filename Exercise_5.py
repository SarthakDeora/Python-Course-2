#Health management system for Harry, Rohan and Hammad

#Make 6 files 2 for each one will have food eaten and one will have exercise done

#1st will ask if wanna see the files or edit the files
print("***************Welcome to our programme***************")
name = input("Who are you?")
if name == "Rohan":
    editorread = int(input("If u wanna edit press 1 if u wanna read then press 0:\n"))
    if editorread == 1:
        foodorexercise = int(input("If u wanna edit food file press 1 and if u wanna edit exercise file then press 0:\n"))
        if foodorexercise == 1:
            with open("RohanFood.txt", "a") as f:
               edit = input("Enter what u wanna add to your file:\n")
               f.write(edit)
        else:
           with open("RohanExercise.txt", "a") as f:
               edit = input("Enter what u wanna add to your file:\n")
               f.write(edit)
    else:
        foodorexercise1 = int(input("If u wanna read food file press 1 and if u wanna read exercise file then press 0:\n"))
        if foodorexercise1 == 1:
           with open("RohanFood.txt") as f:
               f.read()
               print(f)

        else:
           with open("RohanExercise.txt") as f:
               f.read()
               print(f)


elif name == "Harry":
     editorread = int(input("If u wanna edit press 1 if u wanna read then press 0:\n"))
     if editorread == 1:
        foodorexercise = int(input("If u wanna edit food file press 1 and if u wanna edit exercise file then press 0:\n"))
        if foodorexercise == 1:
            with open("HarryFood.txt", "a") as f:
               edit = input("Enter what u wanna add to your file:\n")
               f.write(edit)
        else:
           with open("HarryExercise.txt", "a") as f:
               edit = input("Enter what u wanna add to your file:\n")
               f.write(edit)
     else:
        foodorexercise1 = int(input("If u wanna read food file press 1 and if u wanna read exercise file then press 0:\n"))
        if foodorexercise1 == 1:
           with open("HarryFood.txt") as f:
               f.read()
               print(f)

        else:
           with open("HarryExercise.txt") as f:
               f.read()
               print(f)
elif name == "Hammad":
    editorread = int(input("If u wanna edit press 1 if u wanna read then press 0:\n"))
    if editorread == 1:
        foodorexercise = int(input("If u wanna edit food file press 1 and if u wanna edit exercise file then press 0:\n"))
        if foodorexercise == 1:
            with open("HammadFood.txt", "a") as f:
               edit = input("Enter what u wanna add to your file:\n")
               f.write(edit)
        else:
           with open("HammadExercise.txt", "a") as f:
               edit = input("Enter what u wanna add to your file:\n")
               f.write(edit)
    else:
        foodorexercise1 = int(input("If u wanna read food file press 1 and if u wanna read exercise file then press 0:\n"))
        if foodorexercise1 == 1:
           with open("HammadFood.txt") as f:
               f.read()
               print(f)

        else:
           with open("HammadExercise.txt") as f:
               f.read()
               print(f)
print("***************Thank you for using our programme***************")