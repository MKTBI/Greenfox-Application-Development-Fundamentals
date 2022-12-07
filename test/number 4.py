class CreditCard:
   def __init__(self, provider, transaction_fee, balance = 0):
       self.provider = provider
       self.transaction_fee = transaction_fee
       self.balance = balance
 
   def withdraw(self, amount):
       fee = amount * self.transaction_fee
       if amount + fee > self.balance:
           print('Not enough credit.')
           return  0
       self.balance -= amount + fee
       return amount
 
class MasterCard(CreditCard):
   def __init__(self, balance):
       super().__init__('MasterCard', 0.01, balance)
 
class Visa(CreditCard):
   def __init__(self, balance):
       super().__init__('Visa', 0.02, balance)
 
   def withdraw(self, amount):
       if (amount > self.balance):
           print('Not enough credit.')
           return 0
       self.balance -= amount
       return amount
 
master_card = MasterCard(1000)
visa = Visa(1000)
cash = master_card.withdraw(100) + visa.withdraw(100)
balance = master_card.balance + visa.balance
print(cash, balance)