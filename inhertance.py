class dad():
    def phone(self):
        print("dad phone")

class mom():
    def sweet(self):
        print("mom sweet")


class son(dad,mom):
    def laptop(self):
        print("son laptop")

sandy=son()
sandy.laptop()
sandy.phone()
sandy.sweet()
