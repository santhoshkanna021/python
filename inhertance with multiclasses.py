class grandpa():
    def phone(self):
        print("grandpa phone")
        
class dad(grandpa):
    def money(self):
        print("dad money")

class son(dad):
    def laptop(self):
        print("son laptop")


sandy=son()
sandy.laptop()
sandy.money()
sandy.phone()

