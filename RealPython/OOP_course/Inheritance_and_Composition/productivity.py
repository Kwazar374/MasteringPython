class ProductivitySystem:
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('================================')
        for employee in employees:
            result = employee.work(hours)
            print(f'{employee.name}: {result}')
        print('')

class ManagerRole:
    def work(self, hours):
        return f'{self.name} screams and yells for {hours} hours.'

class SecretaryRole:
    def work(self, hours):
        return f'{self.name} expends {hours} hours doing office paperwork.'

class SalesRole:
    def work(self, hours):
        return f'{self.name} expends {hours} on the phone.'

class FactoryRole:
    def work(self, hours):
        return f'{self.name} manufactures gadgets for {hours} hours.'
