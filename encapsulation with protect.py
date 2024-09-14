class company():
    def __init__(self):
        self._companyName="goooooogle"

class b(company):
    pass

    def companyName(self):
        print(self._companyName)

c1=b()
print(c1._companyName)
