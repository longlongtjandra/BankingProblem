from BankingHomework.BankingClass import *

# customerlist=[]
#
# Bank=Banking()
# Bank.addcustomer("longlong","tjandra")
# Bank.getcustomer().setaccount(1000)
# print(Bank.getcustomer().getaccount().getbalance())
# Bank.listofcustomer()

print("welcome to Bank BCA")

login=input("1.create new account\n2.exit\n")
if login =="1":
    while (login =="1"):
        fname=input("please input your first name:")
        lname=input("please input your last name")
        Bank=Banking()
        Bank.addcustomer(fname,lname)
        initial_deposit=input("please input your initial deposit:")
        Bank.getcustomer().setaccount(initial_deposit)
        action=input("what do you want to do?\n1.deposit\n2.withdraw\n3.info\n4.logout\n")
        while action != "":
            if action== "1":
                deposit=input("how much do you want to deposit?")
                print (Bank.getcustomer().getaccount().deposit(deposit))

            elif action=="2":
                withdraw=input("how much do you want to withdraw?")
                Bank.getcustomer().getaccount().withdraw(withdraw)

            elif action == "3":
                print (Bank.getcustomer().getfname())
                print (Bank.getcustomer().getlname())
                print (Bank.getcustomer().getaccount().getbalance())

            elif action =='4':
                logout=input("are you sure you want to logout?\n1.yes\n2.no\n")
                if logout == "1":
                    print ("thank you for using our service")
                    exit()



                elif logout =="2":
                    continue

            action=input("what do you want to do?\n1.deposit\n2.withdraw\n3.info\n4.logout\n")

elif login== "2":
    print("thank you for using our service")
    exit()


