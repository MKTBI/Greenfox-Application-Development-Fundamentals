'''Create a class named Product that stores
The name of a product
The price of a product
The discount of a product (given in percentage)
Create a method named GetDiscount that returns the following tuple:
The name of the product
The oldPrice of the product
The newPrice of the product which is based on the discount
Test your solution in the Main method'''

class Product:
    def __init__(self,name,price,discount) -> None:
        self.name = name
        self.price = int(price)
        self.discount = int(discount)
    
    def GetDiscount(self):
        old_price = self.price
        new_price = self.price - (self.price * (self.discount / 100))
        return (self.name, old_price, new_price)

if __name__ == "__main__":
    product = Product("Shoes", 100, 20)
    name, old_price, new_price = product.GetDiscount()
    print("Product:", name)
    print("Old price:", old_price)
    print("New price:", new_price)