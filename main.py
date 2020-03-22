#import the class

from CheckingAccount import CheckingAccount

#create an object of CheckingAccount

account1 = CheckingAccount("John Walker","13th Street",3214,60.7)

#perform operation as credit and debit

account1.credtitAccount(44.60)

account1.debitAccount(260.00)

account1.debitAccount(30.00)

#show the balance of the account

account1.showBalance()