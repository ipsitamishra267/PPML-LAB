fruits = ["apple", "banana", "cherry", "mango", "orange"]
print("Original list of fruits:", fruits)

print("\nFruits in reverse order:")
for fruit in fruits[::-1]:
    print(fruit)

print("\nLength of each fruit name:")
for fruit in fruits:
    print(fruit, ":", len(fruit))

reversed_fruits = []
for fruit in fruits:
    reversed_fruits.append(fruit[::-1])

print("\nList containing reversed fruit names:")
print(reversed_fruits)