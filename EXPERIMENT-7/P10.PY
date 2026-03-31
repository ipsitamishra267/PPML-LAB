def sum_of_list(lst):
    total = 0
    for i in lst:
        total += i
    return total

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

result = sum_of_list(lst)
print("Sum of elements:", result)