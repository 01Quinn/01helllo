class Empolyee:
    def __init__(self, first_name, last_name):
        Employee.employee_number = Empolyee.employee_number +1
        self.employee_number = Employee.employee_number
        self.first_name = first_name
        self.last_name = last_name

    def print_information(self):
        print(f"Employee {self.first_name}")

class HourlyPaid:
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def print_information(self):

        print(f"hourly paid {self.salary}")
        print(f"- Benefits: {self.benefits}")

    def can_use_lounge(self):
        return False

class Monthly_Paid(Employee):
    def __init__(self, first_name, last_name, salary, benefits):
        super().__init__(first_name, last_name)
        self.monthly_salary = salary
        self.benefits = benefits
        self.hourly_salary = salary


    def use_benefits(self):
        print(f"{self.benefits} uses benefits {self.benefits}")

employee1 = Empolyee("Juha", "T")
employee1.print_information()

employee2.Hourly_Paid("John", 1200)
employee2.print_information()

employee3 =Monthly_Paid("Peter", 1200, "Benefits")

employee4 = Monthly_Paid("Anna", employee2.hourly_paid * 80, "healthcare")

for employee in [employee1, employee2, employee3]:
    employee.print_information()

