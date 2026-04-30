num = 0
num_quantity = int(input("Enter Number quantity: "))

for i in range (0, num_quantity):
    num += int(input("Enter a Number: "))
print(num)

avg_num = (num / num_quantity)

print(avg_num)
