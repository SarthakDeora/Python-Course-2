l = 4 #This is a global variable itcan be accessed by anything.
c = 8
def example1():
    global c
    f = 5 #This is a local variable it cannot be accessed by anything out of this function.
    print(l) #As l is a global variable it can be accessed ny anything but we cant edit it via functions.
    # now to edit the global variables we do this 
    print(c)
    c = 40
    print(c)
    # l = l+4 #this will throw and error
example1()
