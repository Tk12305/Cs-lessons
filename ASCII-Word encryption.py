message = input("enter a letter: ")

# Encrypt and store
encrypted = ""
for letter in message:
    newcharacter = chr(ord(letter)+8)
    encrypted += newcharacter
    print(newcharacter, end="")

print()  # Blank line to separate

# Decrypt the encrypted message
for letter in encrypted:
    newcharacter = chr(ord(letter)-8)
    print(newcharacter, end="")

print()