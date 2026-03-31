a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print("Before swapping:")
print("a =",a)
print("b =",b)
a = a + b
b = a - b
a = a - b
print("After swapping:")
print("a =",a)
print("b =",b)