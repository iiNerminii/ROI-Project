class MoneyTime():

    def __init__(self, income, expenses, cashFlow, investMent):
        self.income = income
        self.expenses = expenses
        self.cashFlow = cashFlow
        self.investMent = investMent
        

    def myIncome(self):
        self.income = input("What was your total income this month? ")
        if float(self.income) >= 0:
                time_to_earn.myExpenses()
        else:
            print("Incorrect input you need to have earned money or broke even for the calculator to work")
            run(0)

    def myExpenses(self):
        Tax = input("How much did the taxes cost you? ")
        Insurance = input("How much did you spend on insurance? ")
        Utilities = input("How much were utilities? ")
        HOA = input("How much did HOA cost? ")
        Lawn_Snow = input("How much did the lawn or snow cleaning cost? ")
        vacancy = input("How much did you lose if the property was vacant? ")
        repairs = input("How much were repairs? ")
        CapEx = input("How much was spent on Captial Expenditures? ")
        prop_Man = input("How much did managing the property cost? ")
        mortgage = input("How much was your total mortage payment this month? ")
        total_exp =float(Tax) + float(Insurance) + float(Utilities) + float(HOA) + float(Lawn_Snow) + float(vacancy) + float(repairs) + float(CapEx) + float(prop_Man) + float(mortgage)
        self.expenses = (f"Your expenses came to a total of: ${total_exp}")
        print(self.expenses)
        self.expenses = total_exp
        time_to_earn.My_Flow()

    def My_Flow(self):
        flow = float(self.income) - float(self.expenses)
        self.cashFlow = (f"Your total cash flow for this month is: ${flow}")
        print(self.cashFlow)
        self.cashFlow = flow
        time_to_earn.my_investment()

    def my_investment(self):
        Down_pay = input("How much did you put down on the investment? ")
        closing_cost = input("How much were clsoing costs? ")
        rehab_budget = input("How much did you put in for refurbishing? ")
        misc_oth = input("How much were the misc expenses? ")
        total_invest = float(Down_pay) + float(closing_cost) + float(rehab_budget) + float(misc_oth)
        self.investMent = (f"The total you have invested is: ${total_invest}")
        print(self.investMent)
        self.investMent = total_invest
        time_to_earn.total_mon()

    def total_mon(self):
        an_cash = float(self.cashFlow) * 12
        print(f"Your projected annual cash flow is going to be: ${an_cash}!!!")
        my_Roi = float(an_cash) / float(self.investMent) * 100
        print(f"The total ROI will come out to: {my_Roi}% Congrats!!!!")

time_to_earn = MoneyTime(0,0,0,0)

def run(self):
    while True:  
        start_here = input("Welcome to the Total ROI Calculator! Input 'Start' to begin or 'Quit' to leave... ")
        if start_here.lower() == 'start':
            time_to_earn.myIncome()
        elif start_here.lower() == 'quit':
            print("Thank you and Goodbye :) ")
            break
        else:
            print("Sorry we do not understand that input please try again...")

run(0)

