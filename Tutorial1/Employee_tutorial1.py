class Employee:
    def __init__(self,name,id,institute,dept,salary):
        self.name=name
        self.id=id
        self.institute=institute
        self.dept=dept
        self.salary=salary
    def display(self):
        print("Employee details : ",self.name,self.id,self.institute,self.dept,self.salary)
list=[]
list.append(Employee("Anooja",11,"IBM","Management",2000000))
list.append(Employee("Jinu",12,"TCS","Account",500000))
list.append(Employee("Pallavi",13,"Apple","Technical",5000000))
list.append(Employee("Nadhu",14,"Google","SA",8000000))
list.append(Employee("Dilna",15,"Accolite","Cloud techi",900000))
for obj in list:
    if((obj.salary/12) > 100000):
        obj.display()