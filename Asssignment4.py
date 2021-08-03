'''
4. Consider any real time application like banking, college automation, stock market etc.,
   and make use of user defined exceptions according to application and raise that exception.
'''
class WithDrawl_Limit_Exceeded_Exception(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
class Insufficient_Balance_Exception(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
class Banking:
    def __init__(self):
        self.balance = 0
        print('Welcome to Banking World!')
    def Deposit(self):
        Amount = float(input('Enter the Amount to Deposit:'))
        self.balance += Amount
        print('Current Balance is',self.balance)
    def WithDrawl(self):
        try:
            amount = float(input('Enter the Amount to be Withdrawn:'))
            if amount >= 20000 :
                raise WithDrawl_Limit_Exceeded_Exception(amount)
            elif self.balance < amount:
                raise Insufficient_Balance_Exception(amount)
            else:
                self.balance -= amount
        except WithDrawl_Limit_Exceeded_Exception as wle:
            print('WithDrawl amount',amount,'should not be exceeded Code 135')
        except Insufficient_Balance_Exception as ibe:
            print('WithDrawl Amount',amount,'is greater than the original amount and cannoot be withdrawn Code 137')
    def Display_Contents(self):
        print('Net Sufficient Balance is',self.balance)

# Driver Code
Bank = Banking()
Bank.Deposit()
for i in range(2):
    Bank.WithDrawl()
Bank.Display_Contents()
'''
Output:
Welcome to Banking World!
Enter the Amount to Deposit:100000
Current Balance is 100000.0
Enter the Amount to be Withdrawn:20000
WithDrawl amount 20000.0 should not be exceeded Code 135
Enter the Amount to be Withdrawn:10000
Net Sufficient Balance is 90000.0
'''
