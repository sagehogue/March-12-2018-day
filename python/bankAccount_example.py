class BankAccount:
    def __init__(self, n):
        self.name = n
        self.balance = 0

    def greet(self, thing=0):
        return 'Hello {}!'.format(self.name)

    def deposit(self, amt):
        self.balance += amt
        print('Thanks for depositing ${}. Your balance is now {}.'.format(amt, self.balance))

    def withdraw(self, amt):
        if self.balance - amt >= 0:
            self.balance -= amt
            print('You have withdrawn ${}. Your balance is now ${}.'.format(amt, self.balance))
        else:
            print('You don\'t have enough. Your balance is ${}'.format(self.balance))

    def __str__(self):
        return '{}, Balance: {}'.format(self.name, self.balance)

    def _repr__(self):
        return self.__str__()


class BankAccountReserved(BankAccount):
    def __init__(self, n):
        super().__init__(n)

    def withdraw(self, amt):
        if self.balance - amt - 100 >= 0:
            super().withdraw(amt)
        else:
            print(
                'You don\'t have enough. Your balance is ${}.\
                 You must keep at least $100 in your account at all times.'.format(self.balance)
            )


chris = BankAccountReserved('Chris')
chris.balance = 200
sheri = BankAccount('Sheri')
sheri.balance = 2000
accounts = [sheri, chris]
while True:
    q = input('1. New Account:\n2. List Accounts\n9. Quit\n:')
    if q == '1':
        name = input('What is the name for the account?: ')
        new_acc = BankAccount(name)
        accounts.append(new_acc)
        print('A new account has been created for {}'.format(new_acc.name))
    elif q == '2':
        for i in accounts:
            print(i.name, i.balance)
    elif q == '9':
        quit()
    else:
        print('I did not understand that.')


# This is a new line that I am adding