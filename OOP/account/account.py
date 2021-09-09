import uuid

class Account:
    def __init__(self):
        self._id = uuid.uuid1()
        self._balance = 0
        self._rates = 0

    def __str__(self):
        return f"{self._id} : ${self._balance}"


class Customer:
    def __init__(self, name, age, gender, income):
        self.name = name
        self.age = age
        self.gender = gender
        self.income = income
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
    
    def __str__(self):
        return f"{self.name}({self.age}, {self.gender}) : ${self.income}"

    def display_account(self):
        for acc in self.accounts:
            print(acc.__str__)


class Loan:
    OVERDUE_PENALTY = 0.5
    PAYMENT_DAY = 15
    
    def __init__(self):
        self.debt = 0.0
        self.month = 0
        self.loan_interest = 1.0
        
    def loan(self, amount, month):
        self.debt += amount
        self.month = month
    
    def repay(self, amount):
        self.debt -= amount
        return self.debt
    
    def get_payment(self):
        return int(self.debt * (1+self.loan_interest)/self.month)

    def __str__(self):
        return f"total debt : {self.debt}({self.month} month)"

    def adjust_interest(self, interest):
        self.loan_interest = interest
    
    def overdue_penalty(self, penalty):
        self.debt += self.debt * self.OVERDUE_PENALTY
        return self.debt


class Banking:
    def __init__(self):
        self.interest = 1.0
    
    def deposit(self):
        pass

    def withdraw(self):
        pass


class Bank(Banking, Loan):
    def __init__(self):
        Banking.__init__(self)
        Loan.__init__(self)
        self.__accounts = []


class LoanAccount(Account, Bank):
    def __init__(self, owner):
        Account.__init__(self)
        Bank.__init__(self)
        self._owner = owner

    def deposit(self, amount):
        self._balance += amount
        if self.debt > 0:
            payment = self.get_payment()
            print('You have to repay $',payment)
            self._balance -= payment
            self.repay(payment)

    def withdraw(self, amount):
        self._balance -= amount

    def __str__(self):
        return f"{self._owner}\n{super().__str__()}\ntotal debt : {self.debt}({self.month} month)"


if __name__ == '__main__':
    c = Customer('cocoa', 17, 'male', 10000)
    L1 = LoanAccount(c)
    L1.loan(5000, 12)
    L1.deposit(1000)
    print(L1)