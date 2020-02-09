import os
import sys
import cmd

class Account:

    __AccountNumber = 0
    __AccountHolder = ""
    __MoneyDeposited = 0.00
    AccountType = "Savings"

    def __init__(self):
        self.__AccountNumber
        self.__AccountHolder
        self.__MoneyDeposited
        self.AccountType

    def create_account(self, args):
        self.__AccountNumber = int(args[0])
        self.__AccountHolder = args[1]
        self.__MoneyDeposited = int(args[2])
        self.AccountType = args[3]

    
    def modify(self, args):
        self.create_account(args)
        
    
    def accnum(self):
        return self.__AccountNumber
    
    def deposit(self, arg):
        if arg >= 0 :
            balance = self.__MoneyDeposited
            balance = balance + arg
            self.__MoneyDeposited = balance
            print('Successfully deposited {} rupees in your account\n'.format(arg))
        else :
            print('Error. Only enter positive integers\n')
    
    def withdraw(self, arg):
        if arg > self.__MoneyDeposited :
            print("Error. Money exceeded the balance. Cannot Withdraw\n")
        else :
            balance = self.__MoneyDeposited
            balance = balance - arg
            self.__MoneyDeposited = balance
            print("Successfully withdrawn {} from the account\n".format(arg))
    
    def table(self):
        pass

    def accbal(self):
        return self.__MoneyDeposited
    
    def acctype(self):
        return self.AccountType
    
    def accholder(self):
        return self.__AccountHolder
    
    def show_account(self):
        print("\nAccount Number: {}".format(self.__AccountNumber))
        print("Account Holder: {}".format(self.__AccountHolder))
        print("Money Deposited: {}".format(self.__MoneyDeposited))
        print("Account Type: {}\n".format(self.AccountType))
