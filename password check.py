print ("Password checker")

def password_checker(password):
    value = True
    
    if  len(password)<8:
        print ("You need more characters")
        value = False
    
    if not any(char.isdigit() for char in password):
        print ("password should have at least 1 digit")
        value = False
    
    if not any(char.isupper() for char in password):
        print ("password should have at least 1 uppercase")
        value = False

    if not any(char.islower() for char in password):
        print ("password should have at least 1 lowercase")
        value = False
    
    symbol = ["!","@","£","$",".","%","^","&","*","(",")","-","_","=","+","{","}","[","]",":",";","'","<",">",",",".","?","/","|","~","`"]
    
    if not any(char in symbol for char in password):
        print ("you need a symbol !@£$ in your password")
        value = False
    
    if value:
        return value

def menu():
    password = input("What is your password? ")
    if (password_checker(password)):
        print ("Good Password")
    else:
        print ("You should improve Password")

menu()
