class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def change_price(self, new_price):
        self.price = new_price

    def change_quantity(self, new_quantity):
        self.quantity = new_quantity


class Order:
    def __init__(self):
        self.products = []
        self.total = 0

    def add_product(self, product, count):
        if product.quantity >= count:
            self.products.append((product, count))
            product.change_quantity(product.quantity - count)
            self.calculate_total()
        else:
            print(f"Not enough {product.name} in stock!")

    def calculate_total(self):
        self.total = sum(p.price * c for p, c in self.products)


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)


def load_data(filename):
    products = []
    customers = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")
            if parts[0] == "Product":
                products.append(Product(parts[1], parts[2], float(parts[3]), int(parts[4])))
            elif parts[0] == "Customer":
                customers.append(Customer(parts[1], parts[2]))
    return products, customers


# использование 
if __name__ == "__main__":
    products, customers = load_data("data.txt")

    # создаём заказ
    order1 = Order()
    order1.add_product(products[0], 2)  
    order1.add_product(products[1], 1)  

    # добавляем заказ клиенту
    customers[0].add_order(order1)

    print(f"Customer: {customers[0].name}")
    print(f"Total order sum: {order1.total}")
