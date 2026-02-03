#function based program (modularity)

def menu(): #call a function called menu
    print ("""1. are
    2. odd ir even number
    3. multiply number""")

    answer = int(input("Enter number:")) #int whole number
    if answer == 1:
        area()
    if answer == 2:
        odd()
    if answer == 3:
        multiply
    else:
        print("wrong number")

def area(w,h):
    return w*h
x = 5
y = 10

print("Area is",area(x,y)) # calculates area

def odd():
    number = 11
if number == 0:
   print("Even")
else:
    print("Odd")

def multiply(): # if num is less than 5 print num x i
    num=3
    i=1
while i<=5:
     print(num*i)
     i=i+1
 