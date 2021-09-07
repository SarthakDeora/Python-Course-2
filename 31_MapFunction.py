#NOw to apply aa function to every item in a list we use map function 

list1 = ["1","2","3","4","5","6","7","8"]#For example if i want to change these strings into integers 
list1 = list(map(int, list1)) 
print(list1[2] + list1[5])

#For example i make a function that squares the numbers 
def sq(i):
    return i*i

squared_list1 = list(map(sq, list1))#THis was with a function made outside of this function
print(squared_list1)

sqaured_list1_2 = list(map(lambda x: x*x, list1))
print(sqaured_list1_2)
