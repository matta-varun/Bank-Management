KOSS-SELECTION-TASKS 2020

BANK MANAGEMENT

This Repository contains the Program that manages a bank. I have written the entire program in Python and surprisingly this is the first complete program that I have written using Python. It has been only two weeks since I started learning Python, so bear with me any blunders I may have committed in this program. The reason I have chosen Python for this task is that after some research online, I have found that Python contains wide number of packages to create Command Line Interfaces. Though I was still an amateur in Python, I took this as a challenge and as a task to learn new things, and surely I did.

The most time consuming part of the process was narrowing down the packages which implement CLI. First I looked through the ArgParse Module and found it really interesting. The syntax was a little bit complicated to me, as I was a beginner but I was able to get around it.
The trouble arrived when I had to combine classes and ArgParse. Though we can implement basic and simple classes in ArgParse, creating wide and long classes with multiple inputs felt a tedious and hectic job for me. I wasn't very sure and clear about using ArgParse in my code. 

By this time, I have wasted a lot of time. So I quickly started to explore the next Module for creating CLIs, Click Module. It was a great package, with emphasis on appearance and Python Decorators. I felt the same way about this as I felt with ArgParse. It would take a lot more time to master this module and implement it with classes. Frantically, I started searching for much simpler, amateur-friendly modules and then I came across cmd class of Python. I was surprised I didn't come across this all this time. It was simple, elegant to use and I was able to understand the class methods quickly. So I learned all the basic feautures quickly and started implementing in the program.

I first thought of using nested Interpreters for the create_account() method, which would take in AccountNumber, AccountHolder,..etc seperately. Similarly for modify().
I first inserted a cmdloop() in create_account like this:

    i = InfoCmd()
        i.prompt = self.prompt[:-1]+' :CreateAccount) '
        i.cmdloop()
        
The Constructor for this nested Interpreter was:

    import os
    import cmd
    
    class InfoCmd(cmd.Cmd):
    intro = 'Enter the details of the account here.    Type help or ? to list the commands.\n'
    global acc
    
    def do_AccountNumber(self, arg):
        acc = Account()
        acc.create_account().create_accountnumber(arg)
    def do_AccountHolder(self, arg):
        acc = Account()
        acc.create_account().create_accountholder(arg)
    def do_MoneyDeposited(self, arg):
        acc = Account()
        acc.create_account().create_moneydeposited(arg)
    def do_AccountType(self, arg):
        acc = Account()
        acc.create_account().create_accounttype(arg)
    def do_exit(self, *args):
        return True
        
And the method for overwriting the private class attributes was

    def create_account(self):
        def create_accountnumber(self, account_number):
            self.__AccountNumber = account_number
        def create_accountholder(self, account_holder):
            self.__AccountHolder = account_holder
        def create_moneydeposited(self, money_deposited):
            self.__MoneyDeposited = money_deposited
        def create_accounttype(self, acctype):
            self.AccountType = acctype
            
But it was not working at all. TYPE ERRORS were showing up, saying the object was of NONE type and that it doesn't have a create_account() attribute. But clearly according to my knowledge (2 weeks :p) and observance, I was sure it should work. If I have more time, I might have had explored this concept a bit more and realize my mistake. But time was running out. So I scrapped the idea of using nested Interpreters and started to build my code with basic cmd loop that takes one string at a time. I also wanted to include a command completion feature that autocompletes for you on clicking TAB like:

    AVAILABLE_OPTIONS = ('XYZSE', 'AWRPOS', 'WIRIRIE', 'QWPOPOIR', 'PORPSPAS')
    def complete_option(self, text, line, begidx, endidx):
        return [i for i in _AVAILABLE_OPTIONS if i.startswith(text)]
        
But this too was raising many exceptions. So I settled for a simple, very basic CLI that takes in one string at a time.
I overcame the missing fun of using nested interpreters by using  split()  function and passing the list into the method. But this required a specific order of input thus reducing the user-friendliness. I tried to take care of some corner cases like Deposit being negative and Withdraw crossing the balance amount or being negative.

There still is one major bug in this package. SetAccount was meant to shift the default account around the defined Accounts on the basis of their AccountNumbers, which was their key for the dictionary they are stored in. But it doesn't shift the dafault Account to any account, rather it stays with the latest defined Account using CreateAccount(). Tried passing the account set to default into a list defined globally which was then used everywhere else. Still no improvement seen. I thought maybe the account has to be again defined in the SetAccount method(which it shouldn't mostly). I tried, but, no gain. I assume the problem may do with defining global variable object acc and using it along with the other methods. I'm not sure, but I don't have any more time to explore it given that I have 3 class tests in the next three days. 

I know this wasn't a very desirable and likable output but this being my first Python Program I have ever completely written, makes me so happy with how it turned out. Thank you to my interviewers for giving me this task. It was amazing, rigorous and very educating. I have learnt a lot many things and I'd really love to join KOSS and learn a lot many more. Hope for the best.
