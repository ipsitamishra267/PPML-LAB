int_data = int(input("Enter an integer: "))
str_data = input("Enter a string: ")
float_data = float(input("Enter a float: "))
bool_data = input("Enter a boolean(True/False): ")
complex_data = complex(input("Enter a complex number(a+bj): "))
if (bool_data.lower() == "true"):
    bool_data = True
else:
    bool_data = False
print("\nData and their types: ")
print(int_data,"is of type",type(int_data))
print(str_data,"is of type",type(str_data))
print(float_data,"is of type",type(float_data))
print(bool_data,"is of type",type(bool_data))
print(complex_data,"is of type",type(complex_data))