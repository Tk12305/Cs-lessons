fname=input("please type firstname:")
lname=input("please type lastname:")
year=int(input("please input year:"))

user_fname=(fname[:3])
user_lname=(lname[:2])

username = (user_fname+user_lname+"."+(str(year)))
print("Your username is:"+username)