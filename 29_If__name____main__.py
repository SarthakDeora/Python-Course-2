#I will make some functions here so that i can import these functions
#  in other files but this file has some code which i dont want to get imported so
#  in that case we use __main__

def function1(str):
    return "lulam la", str
if __name__ == "__main__":
    print(function("ok"))# i dont want this to imported
    #Now every code under this if statement will not be imported to other files
