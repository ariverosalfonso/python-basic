from employee import Employee, SalaryEmployee, HourleyEmployee, ComissionEmployee

class Company:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
        
    def display_employees(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.fname, i.lname)
        print('-------------------')
    def pay_employees(self):
        print('Paying employees:')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            print('Amount:', i.calculate_paycheck())
        
def main():
    my_company = Company()
    
    employee1 = SalaryEmployee('Sarah', 'Hess', 5000)
    my_company.add_employee(employee1)
    employee2 = HourleyEmployee('Lisa', 'Hess', 25, 50)
    my_company.add_employee(employee2)
    employee3 = ComissionEmployee('Maria', 'Hess',20000, 5,200 )
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()

main()