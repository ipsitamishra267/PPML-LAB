m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100

print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90 and percentage <= 100:
    print("Grade: O")

elif percentage >= 80 and percentage < 90:
    print("Grade: E")

elif percentage >= 70 and percentage < 80:
    print("Grade: A")

elif percentage >= 60 and percentage < 70:
    print("Grade: B")

elif percentage >= 50 and percentage < 60:
    print("Grade: C")

else:
    print("Grade: F")