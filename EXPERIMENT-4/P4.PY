num = int(input("Enter a positive integer: "))
sum_digits = 0

while num > 0:
    sum_digits += num % 10
    num = num // 10

print("Sum of digits:", sum_digits)