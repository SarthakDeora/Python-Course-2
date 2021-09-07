total_rows = int(input("Enter a number:\n"))
condition = int(input("if True type 1 if False type 0:\n"))
conditiontf = bool(condition)
s = total_rows
a=1
star="*"
if condition == 1:
    conditiontf = True

else:
    conditiontf = False

# print(conditiontf)

if conditiontf == True:
    while a<=total_rows:
        
        print(star*a)
        a=a+1
else:
    while s >= 0:
        print(star*s)
        s = s-1


# it would have been easy i knew for loop also exists 