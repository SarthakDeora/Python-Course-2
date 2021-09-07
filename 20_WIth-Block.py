#Now openenig and closing a file is a kinda lengthy to do and we sometimes forget it
#so to do it easily we use with open
with open("sarthak.txt") as f:
    a = f.read(4)
    print(a)