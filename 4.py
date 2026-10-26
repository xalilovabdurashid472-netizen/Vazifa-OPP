class Ticket:
    def __init__(self,film,price,count):
        self.film=film
        self.price=price
        self.count=count
    def total_cost(self):
        return self.price*self.count
    def show_info(self):
        print(f"Film: {self.film}")
        print(f"Umumiy xarajatlar: {self.total_cost()} som")
ticket = Ticket("Avatar", 40000, 3)
print(ticket.total_cost())
ticket.show_info()