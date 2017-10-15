class Account:
    def __init__(self,balance):
        self.__balance=float(balance)

    def getbalance(self):
        return self.__balance

    def deposit(self,deposit):
        if(int(deposit) < 0):
            print ("amount can not be lower than 0")
            return False

        else:
            new_balance=self.__balance+int(deposit)
            self.__balance=new_balance
            print("deposit succesful")
            return True

    def withdraw(self,withdraw):
        if(int(withdraw)>self.__balance):
            print("insufficient fund")
            return False
        elif(int(withdraw)<0):
            print("amount cant be lower then 0")
            return False

        else:
            new_balance=self.__balance-int(withdraw)
            self.__balance=new_balance
            print ("withdraw succesful")
            return True




