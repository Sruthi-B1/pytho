from datetime import date
from datetime import datetime
import datetime
class Employee:
    def _init_(self,empid,name,salary,insurance):
        self.empid=empid
        self.name=name
        self.salary=salary
        self.insurance=insurance


class Personal:
    def _init_(self,status,nomininame,dob):
        self.status=status
        self.nomininame=nomininame
        self.dob=dob



class Insurance(Employee,Personal):
    def _init_(self,empid,name,salary,insurance,status,nomininame,dob):
        Employee._init_(self,empid,name,salary,insurance)
        Personal._init_(self,status,nomininame,dob)

    def display(self):
        today = date.today()
        # print("Today's date:", today)
        age= today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        sam=self.status
        if age >=18 and (sam ==False):
            amt=self.insurance*12*12
            print(self.nomininame,amt)


dob = datetime.date(1982,8,7)
# birthday = input("Enter your date of birth: ")

# bday = datetime.strptime(birthday, '%d/%m/%Y')
today = date.today()
# print("Today's date:", today)

age= today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
# print(age)


s1=Insurance(101,'Rahul',100000,2000,False,"Jibin",dob)
s1.display()