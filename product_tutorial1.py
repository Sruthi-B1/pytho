class Product: 
    def __init__(self,pcode,pname,price,fruit,cosmetic):
        self.pcode = pcode
        self.pname = pname 
        self.price = price 
        self.fruit = fruit
        self.cosmetic = cosmetic
    def display(self):
        print("Pcode : ",self.pcode) 
        print("Pname : ",self.pname) 
        print("Price : ",self.price) 
list = [] 
list.append(Product(3001,"Banana",850,True,True))
list.append(Product(3002,"Cherry",820,True,False))
list.append(Product(3003,"Lemon",680,True,True)) 
for p in list:
    if(p.fruit and p.cosmetic ):
        p.display()
        
        
        
    