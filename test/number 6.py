class Restaurant:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.income = 0
        self.no_of_customers = 0
        self.list_of_customers = []

    def sit(self, *customers):
        self.no_of_customers = self.no_of_customers + len(customers)
        self.list_of_customers.extend(customers)

    def serve_menu(self):
        answer = []
        for cust in self.list_of_customers:
            if isinstance(cust, Employee):
                answer.append(f"{cust.name} is eating for {self.cost // 2}")
                self.income += self.cost // 2
            elif isinstance(cust, Guest):
                answer.append(f"{cust.name} is eating for {self.cost}")
                self.income += self.cost

        self.no_of_customers = 0
        print("\n".join(answer))

    def __str__(self):
        return f"{self.name} | {self.no_of_customers} customers | menu for {self.cost}$ | income:  {self.income} "


class Employee:
    def __init__(self, name):
        self.name = name


class Guest:
    def __init__(self, name):
        self.name = name


john = Employee('John')
jane = Guest('Jane')
restaurant = Restaurant('Galactica', 10)
print(restaurant) # should print: Galactica | 0 customers | menu for 10$ | income: 0
restaurant.sit(john, jane)
print(restaurant) # should print: Galactica | 2 customers | menu for 10$ | income: 0
restaurant.serve_menu() # should print: John is eating for 5.0\nJane is eating for 10
print(restaurant) # should print: Galactica | 0 customers | menu for 10$ | income: 15