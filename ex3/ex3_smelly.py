class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self):
        discounted_price = self.price - (self.price * self.discount_rate)
        print(f"Discounted price for {self.name} ({self.__class__.__name__}): {discounted_price}")
        return discounted_price
    
    def calculate_tax(self):
        tax = self.price * self.tax_rate
        print(f"Tax for {self.name} ({self.__class__.__name__}): {tax}")
        return tax

class Electronics(Item):
    discount_rate = 0.10 # 10% discount
    tax_rate = 0.15 # 15% tax

class Clothing(Item):
    discount_rate = 0.20 # 20% discount
    tax_rate = 0.08 # 8% tax

class Grocery(Item):
    discount_rate = 0.05 # 5% discount
    tax_rate = 0.02 # 2% tax

