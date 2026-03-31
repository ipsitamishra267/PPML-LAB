import math
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
S = perimeter/2
area = math.sqrt(S*(S-a)*(S-b)*(S-c))
print("Perimeter of the triangle:",perimeter)
print("Area of the triangle:",area)