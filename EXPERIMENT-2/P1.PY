p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of interest: "))
t = float(input("Enter Time(in years): "))

simple_interest = (p*r*t)/100
amount = p*(1+r/100)**t
compound_interest = amount - p
print("Simple Interest:",simple_interest)
print("Compound Interest:",compound_interest)