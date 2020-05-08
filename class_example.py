class worker:
    def __init__(self, name, pay):
        self.name=name
        self.pay=pay
    def getname(self):
        print(self.name)
    def getpay(self):
        print(self.pay)
    def updatepay(self,amount):
        self.pay=amount

ID1293389=worker('Diego Sanchez',25000)
ID1293389.getname()
ID1293389.getpay()
ID1293389.updatepay(30000)
ID1293389.getpay()

        
