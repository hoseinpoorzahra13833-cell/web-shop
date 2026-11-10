class Product:
    def init(self, sku, name, price):
        if not sku:
            raise ValueError("sku is required")
        self.sku = sku
        self.name = name
        self.price = price


def find_by_name(products, text):
    return [p for p in products if text.lower() in p.name.lower()]

# Lab 2 commit A

def apply_discount(price, percent):
    return price * (100 - percent) /100

def add_tax(price, rate=0.2):
    return price * (1 + rate)