class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, name, price, category):
        self.products.append(Product(name, price, category))
        return self

    def sell_product(self, id):
        self.product.print_info
        del self.products[id]
        return self

    def product_info(self,name):
        for i in self.products:
            if i.this_name == name:
                i.print_info()

class Product:
    def __init__(self, name, price, category):
        self.this_name = name
        self.this_price = price
        self.this_category = category

    def update_price(self, percent_change, is_increased):
        if is_increased is True:
            temp = self.this_price * percent_change
            self.this_price = self.this_price + temp
        else:
            temp = self.this_price * percent_change
            self.this_price = self.this_price - temp
        return self

    def print_info(self):
        print(f"\nName of Product: {self.this_name} \nCategory of Product: {self.this_category} \nPrice of Product: {self.this_price} \n")
        return self



kbtoys = Store("KB Toys")

# car = Product("car", 5, "toy")
# figure = Product("figure", 10, "toy")
# bike = Product("bike", 100, "toy")

kbtoys.add_product("car", 5, "toy").product_info("car")

# car.print_info()
# figure.print_info()
# bike.print_info()

