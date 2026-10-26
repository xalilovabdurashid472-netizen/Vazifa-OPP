class Contact:
    def __init__(self,ism,raqam):
        self.ism=ism
        self.raqam=raqam
    def update_phone(self,yangi):
         self.raqam=yangi
    def show_info(self):
            print(f"Ism: {self.ism}")
            print(f"Telefon: {self.raqam}")
contact = Contact('Malika', '901234567')
contact.update_phone('931112233')
contact.show_info()