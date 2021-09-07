#ARGS helps in adding stuff quiclkly in a function without giving an extra variable.
def function_args(*listone):
    for item in listone:
        print(item)
list1 = ["Mouse", "Keyboard", "controllers"] 

function_args(*list1)
#Kwargs is for dictionaries 
def function_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
dict1 = {"key": "lock", "value": "number"}
function_kwargs(**dict1)