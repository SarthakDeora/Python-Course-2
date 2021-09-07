list1 = ["Asus","Lenovo","HP","Apple","Dell","Acer","Compaq","HCL","Samsung","Realme","Honor"]
#TO join "And" before every item in the list i can use for loop 
for item in list1:
    print(f"{item} and", end = " ")#It took 2 lines
print()
#Python has a in built function to do this in 1 line
a = " and ".join(list1)
print(a)#Well this also took 2 lines but still this is better as in the for loop and comes in the last too