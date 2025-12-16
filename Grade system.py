for x in range (5):
 name = input("Enter your name: ")
 grade = input("grade:")

with open("Grades.txt", "a") as file:
    file.write(f"{name}: {grade}\n")