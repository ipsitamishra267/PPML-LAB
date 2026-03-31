num = int(input("Enter a number: "))
original_num=num
reverse = 0
while num > 0:
    digit = num%10
    reverse = reverse * 10 + digit
    num = num//10
    print("Reverse of",original_num,"is",reverse)
