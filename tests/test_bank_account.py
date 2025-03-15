import unittest
from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):

    def setUp(self):
         self.account=BankAccount(balance=1000)
    
    def test_deposit(self):
       
        balance=self.account.deposit(500)
        assert balance==1500

    def test_withdraw(self):
         
        balance=self.account.withdraw(200)
        assert balance==800

    def test_get_balance(self):
       
        assert self.account.get_balance()==1000


        
