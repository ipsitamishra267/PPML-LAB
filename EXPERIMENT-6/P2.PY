dict1 = {}

n = int(input("Enter number of key-value pairs: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

dict2 = {}

for key, value in dict1.items():
    dict2[value] = key

print("\nFirst Dictionary:")
print(dict1)

print("\nSecond Dictionary (values as keys and keys as values):")
print(dict2)