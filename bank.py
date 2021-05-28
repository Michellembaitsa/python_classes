class Bank:
    def __init__(self,owner,acc_No,type):
        self.owner=owner
        self.acc_No=acc_No
        self.type=type
    def withdraw(self):
        return f"{self.owner} of account number {self.acc_No} has withdrawn KES 2000"
    def balance(self):
        return f"The account {self.acc_No} is a {self.type} type of account"