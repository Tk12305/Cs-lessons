with open("nevergiveup.txt","r") as file:
    content = file.read()
    print (content)

user = input("enter story:")
with open("nevergiveup.txt","a") as file:
    file.write(user)

with open("nevergiveup.txt","r") as file:
    content = file.readlines()
    
    print (content)