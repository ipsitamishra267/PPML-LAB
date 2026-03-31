numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

print("Original list:", numbers)

numbers = list(set(numbers))

numbers.sort()

print("List after removing duplicates and sorting:", numbers)