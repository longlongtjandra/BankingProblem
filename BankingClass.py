from BankingHomework.CustomerClass import Customer

class Banking:
    def __init__(self):
        self.__Bankname="Bank BCA"
        self.__numofcustomer=0
        self.__customer=[]


    def addcustomer(self,fname,lname):
        if fname not in self.__customer and lname not in self.__customer:
            self.__cstmr=Customer(fname,lname)
            self.__customer.append(Customer(fname,lname))
            self.__numofcustomer+=1
            return True

        elif fname in self.__customer and lname in self.__customer:
            print("user already exist")
            return False


    def getnumofcustomer(self):
        return self.__numofcustomer

    def getcustomer(self):
        return self.__cstmr
    # def customer(self,customerlist):
    #     print str(customerlist[0])

    def listofcustomer(self):
        print (self.__customer)






