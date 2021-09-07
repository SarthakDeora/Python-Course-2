list1 = ["Potato", "Tomato", "Cucumber", "Mango", "Banana"] 
#You have to only buy the stuff at even number 
i = 0
for item in list1:
    if i%2 != 0:
        print(f"{item}")
    i+=1

for index, item in enumerate(list1): #Enumerate function gives u the index of the item in the list
    if index%2==0:
        print(f"{item}")

