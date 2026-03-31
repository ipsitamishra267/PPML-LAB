sentence = input("Enter a sentence: ")

list1 = sentence.split()

print("\nElements of list1 with index:")
for index, word in enumerate(list1):
    print(index, ":", word)

list2 = list(range(1, len(list1) + 1))

print("\nList2 (series of numbers):")
print(list2)

list3 = list(zip(list1, list2))

print("\nCombined List (List3):")
print(list3)