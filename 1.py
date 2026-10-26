class Athlete:
    def __init__(self,ismi,sport,yoshi):
        self.ismi=ismi
        self.sport=sport
        self.yoshi=yoshi
    def show_info(self):
        print(f"Ism: {self.ismi}")
        print(f"Sport turi: {self.sport}")
        print(f"Yosh: {self.yoshi}")
athlete=Athlete('Ali', 'Futbol', 20)
athlete.show_info()