text = input("Enter a paragraph: ")

words = text.split()

print("Number of words:", len(words))

palindrome_count = 0

for word in words:
    if word.lower() == word.lower()[::-1]:
        palindrome_count += 1

print("Number of palindromes:", palindrome_count)

print("Words in reverse order:")
for word in words:
    print(word[::-1])