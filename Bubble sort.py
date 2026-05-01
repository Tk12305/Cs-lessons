def bubble_sort(arr):  # Function to perform bubble sort
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Get user input for the array
print("Enter numbers to sort (press Enter after each number, type 'done' when finished):")
my_list = []
while True:
    user_input = input()
    if user_input.lower() == 'done':
        break
    try:
        number = int(user_input)
        my_list.append(number)
    except ValueError:
        print("Please enter a valid number or 'done' to finish.")

# Sort the list
sorted_list = bubble_sort(my_list)
print("Sorted list:", sorted_list)

