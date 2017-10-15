from BankingHomework.AccountClass import Account

class Customer:
    def __init__(self,fname,lname):
        self.__fname=fname
        self.__lname=lname

    def getfname(self):
        return self.__fname

    def getlname(self):
        return self.__lname

    def getaccount(self):
        return self.__acc

    def setaccount(self,balance):
        self.__acc=Account(balance)


