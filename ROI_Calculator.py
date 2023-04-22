class ROI():
    
    def __init__(self):
        rental_income = (float(input('Type in your monthly rental income:  ')))
        laundry_income = (float(input('Type in your monthly laundry income:  '))) 
        storage_income = (float(input('Type in your monthly storage income:  ')))
        # Monthly Expenses
        tax = float(input('Type in your monthly tax expense:  '))
        insurance = float(input('Type in your total monthly insurance:  '))
        # Utilities
        electric = float(input('Type in your monthly electric utilities:  '))
        water = float(input('Type in your monthly water utilities:  '))
        sewer = float(input('Type in your monthly sewer utilities:  '))
        garbage = float(input('Type in your monthly garbage utilities:  '))
        gas = float(input('Type in your monthly gas expense:  ')) 
        hoa = float(input('Type in your monthly HOA fee:  ')) 
        vacancy = float(input('Type in your monthly vacancy expense:  ')) 
        repair = float(input('Type in your monthly repair expenses:  '))
        capital_expenditures = float(input('Type in your monthly capital expenditures:  '))
        property_management = float(input('Type in your monthly property management expense:  '))   
        mortgage  = float(input('Type in your monthly mortgage expense:  ')) 
        self.rental_income = rental_income
        self.laundry_income = laundry_income
        self.storage_income = storage_income
        # Investment
        down_payment  = float(input('Type in your down payment:  '))
        closing_costs = float(input('Type in your closing costs:  '))   
        rehab_budget = float(input('Type in your rehab budget:  '))
        # Expenses
        self.tax = tax
        self.insurance = insurance
        self.electric = electric
        self.water = water
        self.sewer = sewer
        self.garbage = garbage
        self.gas = gas
        self.hoa = hoa
        self.vacancy = vacancy
        self.repair = repair
        self.capital_expenditures = capital_expenditures
        self.property_management = property_management
        self.mortgage = mortgage
        # Investment
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.rehab_budget = rehab_budget

    def cashFlow(self):
        monthly_income = self.rental_income + self.laundry_income + self.storage_income
        monthly_expenses = self.tax + self.insurance + self.electric + self.water + self.sewer + self.garbage + self.gas + self.hoa + self.vacancy + self.repair + self.capital_expenditures + self.property_management + self.mortgage
        cash_flow = monthly_income - monthly_expenses
        return cash_flow
    
    def calculate_roi(self):
        monthly_cash_flow = self.cashFlow()
        total_investment = self.down_payment + self.closing_costs + self.rehab_budget
        roi = (((monthly_cash_flow * 12) / total_investment) * 100)
        return f'Your ROI is {roi}%'
    
final_calculation = ROI()
print(final_calculation.calculate_roi())

# EXAMPLE OUTPUT FROM THE VIDEO
# Income
# Rental income = 2000
# Laundry = 
# Storage = 
# MISC =
# Total monthly income = 2000

# Expenses 
# Tax = 150
# Insurance = 100
# Utilities: 0
#     Electirc
#     Water
#     Sewer
#     Garbage
#     Gas
# HOA  = 0
# Lawn/snow = 0
# Vacancy = 100
# Repairs = 100
# Capital_expenditures = 100
# Property_management = 200
# Mortage: 860
# Total Expenses = 1610

# Cash Flow
# Income - Expenses = 2000 - 1610 = 390, Total Cash_flow  

# Cash_on_Cash ROI 
# Down_payment = 40000
# Closing_costs = 3000
# Rehab_budget = 7000
# MISC other = 0
# Total_Investment = 50000

# Total Monthly Cashflow to year * 12 = 4680
# Annual Cash_Flow / Total investment = 4680 / 50000 = 9.36%
# Cash on Cash ROI 9.36%
