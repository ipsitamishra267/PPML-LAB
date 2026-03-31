class Product:
    def __init__(self, product_id, product_name, price, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.total_amount = 0

    def calculate_total(self):
        self.total_amount = self.price * self.quantity

    def Display(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total Amount:", self.total_amount)


pid = input("Enter Product ID: ")
pname = input("Enter Product Name: ")
price = float(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))

p = Product(pid, pname, price, quantity)

p.calculate_total()
p.Display()