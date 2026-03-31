def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest: "))
t = float(input("Enter Time(in years): "))
si = simple_interest(p, r, t)
print("Simple Interest is:", si)