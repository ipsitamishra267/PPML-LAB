class Employee:
    def __init__(self, empid, name, basic):
        self.empid = empid
        self.name = name
        self.basic = basic
        self.ta = 0
        self.da = 0
        self.gross = 0

    def calc(self):
        self.ta = 0.10 * self.basic
        self.da = 0.40 * self.basic
        self.gross = self.basic + self.ta + self.da

    def disp(self):
        print("Employee ID:", self.empid)
        print("Name:", self.name)
        print("Basic Pay:", self.basic)
        print("TA:", self.ta)
        print("DA:", self.da)
        print("Gross Pay:", self.gross)


empid = input("Enter Employee ID: ")
name = input("Enter Name: ")
basic = float(input("Enter Basic Pay: "))

e1 = Employee(empid, name, basic)
e1.calc()
e1.disp()