
class Player:
    def __init__(self, oyinchi):
        self.oyinchi = oyinchi
        self.energiya = 100

    def use_energy(self, amount):
        self.energiya = max(0, self.energiya - amount)

    def show_status(self):
        print(f"O‘yinchi: {self.oyinchi}")
        print(f"Energiya: {self.energiya}")


player = Player('Hero')
player.use_energy(35)
player.show_status()
