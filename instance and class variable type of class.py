class phone():
    chargertype="c-type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        
    def display(self):
        print("brand:",self.brand)
        print("price:",self.price)
        print("chargertype:",self.chargertype)

phone.chargertype="b-type"
iphone = phone("iphone","20000")
iphone.display()


redmi = phone("redmi","21000")
redmi.display()


nokia = phone("redmi","22000")
nokia.display()


        
        
