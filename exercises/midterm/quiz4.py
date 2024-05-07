class MyCompany:
    def __init__(self, NumberOfEmployess, SalaryPerEmployees, Revenue):
        self.NumberOfEmployess= NumberOfEmployess
        self.SalaryPerEmployees = SalaryPerEmployees
        self.Revenue = Revenue
    def Profit_Calculator(self):
        netProfit = self.Revenue - (self.NumberOfEmployess * self.SalaryPerEmployees)
        print(f"{netProfit}")

company1 = MyCompany(100,1000,1000000)
company1.Profit_Calculator()