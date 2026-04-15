message = input("enter a letter: ")

for letter in message:
    newcharacter = chr(ord(letter)+8)
    print (newcharacter, end="")


for letter in message:
    newcharacter = chr(ord(letter)-8)
    print (newcharacter, end="")