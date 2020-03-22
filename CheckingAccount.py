class CheckingAccount:

   

    #constructor

    def __init__(self,name,address,accountnumber,balance):

        #private variable by using __

        self.__name = name;

        self.__address = address

        self.__acoountNumber = accountnumber

        self.__balance = balance

   

    #perform credit operation on the account

    def credtitAccount(self,amount):

        self.__balance = self.__balance + amount

   

    #perform debit operation on the account

    def debitAccount(self,amount):

        if self.__balance < amount:

            print("Balance (${:.2f}) is low. Debit operation can not be performed for amount ${:.2f}!!!".format(self.__balance,amount))

        else:

            self.__balance = self.__balance - amount

   

    def showBalance(self):

        print("Balance of the account number {} is ${:.2f}, which is in name of {}.".format(self.__acoountNumber,self.__balance,self.__name))