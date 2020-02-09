import os
import sys
import cmd
from classmodule import Account

my_dict = {}
my_list = []
acc = Account()

class BankManagement(cmd.Cmd):
    intro = '\nWelcome to Bank Of Kgp!\nIf you are new here, create your account first.\nThen Set your account as the default one using SetAccount.\n\vType help or ? to list the commands.\n'
    prompt = '(Bank_Of_Kgp) '
    file = None

    def do_CreateAccount(self, args):
        'To create a new account, enter in the order of Account number, Account Holder, Money Deposited and Account Type\n'
        global acc
        global my_dict
        args = args.split()
        acc.create_account(args)
        a = acc.accnum()
        my_dict[str(a)] = acc

    
    def do_ShowAccount(self, arg):
        'Displaying the account details'
        (my_list[0]).show_account()
    
    def do_ModifyAccount(self, args):
        'Enter all the new values for the account'
        global acc
        global my_dict
        global my_list
        del my_dict[str(acc.accnum())]
        args = args.split()
        my_list[0].modify(args)
        my_dict[str(acc.accnum())] = acc

    def do_SetAccount(self, arg):
        'Setting default account. Enter the account number of the account.'
        global my_list
        global my_dict
        global acc
        my_list.clear()
        acc = my_dict[arg]
        my_list.append(acc)



    def do_Deposit(self, arg):
        'Enter money to deposit in your account'
        my_list[0].deposit(int(arg))

    def do_Withdraw(self, arg):
        'Enter money to withdraw from your account'
        my_list[0].withdraw(int(arg))
    
    def do_TabularData(self):
        my_list[0].table()

    def do_ReturnAccNo(self, arg):
        '\nDisplays your account number'
        print("\nYour Account Number is {}\n".format(my_list[0].accnum()))
    
    def do_ReturnAccType(self, arg):
        '\nDisplays the type of your account'
        print("\nYour Account Type is {}\n".format(my_list[0].acctype()))
    
    def do_ReturnAccBal(self, arg):
        '\nDisplays the Balance in your Account'
        print("\nThe Balance in your account is {}\n".format(my_list[0].accbal()))

    def emptyline(self):
        pass
    
    def do_exit(self, s):
        return True

def parse(arg):
        'Convert a series of zeroes or more numbers to an argument tuple'
        return tuple(map(int, arg.split()))

if __name__ == '__main__':
    BankManagement().cmdloop()