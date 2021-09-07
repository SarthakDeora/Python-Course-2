# Now to add something in a string u can:
import math
str1 = "My"
str2 = "name"
print(str1, str2)
str3 = "is"
str4 = "my name %s"%(str3)
print(str4)
str5 = "My name is {} {}"
str6 = str5.format("sarthak", "deora")
print(str6)
# Now F string
class1 = 9
Fstr = f"{str6} And i am in class {class1} and th factorial of 5 is {math.factorial(5)}"#Its easir to add variables in a string with this 
print(Fstr)
    
