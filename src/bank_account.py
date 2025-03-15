class BankAccount:
    def __init__(self,balance=0,log_file=None):
        self.balance=balance
        self.log_file=log_file
        self._log_transaction('Cuenta Creada')

    def _log_transaction(self,message):
        if self.log_file:
            with open(self.log_file,'a') as f:
                f.write(f"{message }\n")

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            self._log_transaction(f"Deposito {amount}. Nuevo Balance :{self.balance}")
        return self.balance
    
    def withdraw(self,amount):
        if amount>0:
            self.balance-=amount
            self._log_transaction(f"Retiro {amount}. Nuevo Balance :{self.balance}")
        return self.balance
    
    def get_balance(self):
        self._log_transaction(f"Consulta de Balance :{self.balance}")
        return self.balance