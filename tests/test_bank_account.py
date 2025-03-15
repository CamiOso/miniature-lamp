import unittest,os
from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):

    def setUp(self):
         self.account=BankAccount(balance=1000,log_file='transaction_log.txt')

    def tearDown(self)->None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self,filename):
        with open(filename,"r") as f:
          return len(f.readlines())

    
    def test_deposit(self):
       
        balance=self.account.deposit(500)
        assert balance==1500

    def test_withdraw(self):
         
        balance=self.account.withdraw(200)
        assert balance==800

    def test_get_balance(self):
       
        assert self.account.get_balance()==1000

    def test_transaction_log(self):
        self.account.deposit(500)
        assert os.path.exists("transaction_log.txt")

    def test_count_transaction_log(self):
        assert self._count_lines(self.account.log_file)==1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file)==2

        
