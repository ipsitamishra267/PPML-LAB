my_list  = [10, 20, 30, 40]
my_tuple = (1, 2, 3, 4)
my_dict  = {1: "Apple", 2: "Banana", 3: "Mango"}
my_set   = {5, 10, 15, 20}

print("\nElements of List:")
for item in my_list:
    print(item)

print("\nElements of Tuple:")
for item in my_tuple:
    print(item)

print("\nElements of Dictionary:")
for key, value in my_dict.items():
    print(key, ":", value)

print("\nElements of Set:")
for item in my_set:
    print(item)