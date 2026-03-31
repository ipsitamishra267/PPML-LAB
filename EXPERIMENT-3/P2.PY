import math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

d= b*b-4*a*c
if d>0:
    r1 = (-b+math.sqrt(d))/(2*a)
    r2 = (-b+math.sqrt(d))/(2*a)
    print("Two distinct real roots")
    print("Root1=",r1) 
    print("Root2=",r2)
elif d==0:
    r = -b/(2*a)
    print("Two equal real roots")
    print("Root=",r)
else:
    real = -b/(2*a)
    imag=math.sqrt(-d)/(2*a)
    print("Complex roots")
    print("Root1=",real,"+",imag,"i")
    print("Root2=",real,"+",imag,"i")