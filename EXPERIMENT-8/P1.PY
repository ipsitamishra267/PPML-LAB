M = int(input("Enter starting number (M): "))
N = int(input("Enter ending number (N): "))

numbers = []

for i in range(M, N+1):
    numbers.append(i)
total = sum(numbers)
average = total / len(numbers)
largest = max(numbers)
smallest = min(numbers)

print("List:", numbers)
print("Sum:", total)
print("Average:", average)
print("Largest:", largest)
print("Smallest:", smallest)

new_list=[]
for num in numbers:
    if num%3!=0:
        new_list.append(num)
print("List without numbers divisible by 3:",new_list)