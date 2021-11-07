from datetime import date
from datetime import datetime
import datetime
class Employee:
    def _init_(self,empid,name,salary,insurance):
        self.empid=empid
        self.name=name
        self.salary=salary
        self.insurance=insurance
class Nominee:
    def _init_(self,status,nomininame,dob):
        self.status=status
        self.nomininame=nomininame
        self.dob=dob
class Insurance(Employee,Nominee):
    def _init_(self,empid,name,salary,insurance,status,nomininame,dob):
        Employee._init_(self,empid,name,salary,insurance)
        Nominee._init_(self,status,nomininame,dob)
    def display(self):
        today = date.today()
        age= today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        sam=self.status
        if age >=18 and (sam ==False):
            amt=self.insurance*12*12
            print(self.nomininame,amt)
dob = datetime.date(1999,3,9)
today = date.today()
age= today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
s1=Insurance(2001,'Sruthi',300000,2000,False,"Bindhu",dob)
s1.display()