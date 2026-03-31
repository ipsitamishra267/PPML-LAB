class Addition:
    def addition(self, a, b):
        print("Addition =", a + b)

class Subtraction:
    def subtraction(self, a, b):
        print("Subtraction =", a - b)

class Multiplication:
    def multiplication(self, a, b):
        print("Multiplication =", a * b)

class Division:
    def division(self, a, b):
        print("Division =", a / b)

class Calculator(Addition, Subtraction, Multiplication, Division):
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

obj = Calculator(a, b)

obj.addition(obj.data1, obj.data2)
obj.subtraction(obj.data1, obj.data2)
obj.multiplication(obj.data1, obj.data2)
obj.division(obj.data1, obj.data2)