from datetime import datetime
class Account: #if it is more than 2 names,make both capital e.g BankAccount
    def __init__(self,name,phone,transactions):
        self.name=name
        # self.acc_No=acc_no
        # self.type=type
        self.phone=phone
        self.balance=0
        self.loan=0
        self.loan_limit=500
        self.transactions=[]


    # def withdraw(self):
    #     return f"{self.name} of account number {self.acc_no} has withdrawn KES 2000"
    # def check_balance(self):
    #     return f"The account {self.acc_No} is a {self.type} type of account"
    def deposit(self,amount):
        if amount<=0:
            return f"Amount must be greater than 0."  #If you do not set this condition, deposits of negatives will minus from acc
        else:
            self.balance+=amount
            transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Deposit"}
            self.transactions.append(transaction)
            # return f"Dear {self.name} you have deposited {amount},your new balance is KSH{self.balance}"
            # return f"Dear {self.name} you made the following transaction {self.transactions}"
    def show_balance(self):
        return self.balance
    def withdraw(self,amount):
        if amount<=0:
            return f"amount must be greater than zero"
        elif amount>self.balance:
            return f"You can not withdraw KES {amount},available balance is {self.balance}"
        else:
            self.balance-=amount
            transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Withdraw"}
            self.transactions.append(transaction)
            return f"You have withdrawn {amount},your balance is KES{self.balance}"

    def borrow(self,amount):
        if amount<=self.loan_limit:
            self.loan+=amount
            self.balance+=self.loan
            transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Loan"}
            self.transactions.append(transaction)
            return f"Dear {self.name}, you have borrowed KES{amount}.Your loan of {self.loan} is due on September 1st,your balance is KES{self.balance}"
        else:
            return f"Your loan request of KES{amount} is unsuccessful because your loan limit is {self.loan_limit}"

    def get_statement(self):
        for transaction in self.transactions:
            narration=transaction["narration"]
            amount=transaction["amount"]
            balance=transaction["balance"]
            time=transaction["time"]
            print(f"{time.strftime('%D')}..{narration}..{amount}..{balance}..")
    def repay_loan(self,amount):
        if amount<0:
            return "Dear {self.name} amount has to be more than 0."
        elif amount<self.loan:
            self.loan-=amount
            return f"{amount} has been repaid to your loan of KES {self.loan} "
        else:
            extra=amount-self.loan
            self.balance+=extra
            transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Payments"}
            self.transactions.append(transaction)
            return f"Your loan has been fully paid.Your account balance is {self.balance}"
