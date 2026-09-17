class Account :
    def setmoney(self):
        print("override  me !!")

    def get_status(self):
        print("print as it is !!")

acc=Account()
acc.setmoney()
acc.get_status()