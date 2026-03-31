a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

min_num = min(a, b, c)

while min_num > 0:
    if a % min_num == 0 and b % min_num == 0 and c % min_num == 0:
        print("GCD of", a, b, c, "is", min_num)
        break
    min_num -= 1