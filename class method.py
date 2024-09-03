class laptop():
    chargertype="c-type"

    def __init__(self):
        self.brand=""
        self.price="32"

    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)


    @classmethod
    def chargertype(cls):
        cls.chargertype="b-type"
        print("the charger type was change")

    @staticmethod
    def info():
         print("this the laptop class")
   

hp=laptop()
hp.setprice(7537578)
hp.getprice()


laptop.chargertype()

laptop.info()
