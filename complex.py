class Complex:
    def initComplex(self):
        self.x = int(input("Enter the Real Part: "))
        self.y = int(input("Enter the Imaginary Part: "))            
    def display(self):
        print(self.x,"+",self.y,"i", sep="")

    def addition(self,c1,c2):
        imaginary=c1.x+c2.x
        realpart=c1.y+c2.y
        
        print("addition-total:",imaginary,"+","i",realpart,sep="")
    
    def substraction(self,c1,c2):
        imaginary=c1.x-c2.x
        realpart=c1.y-c2.y
               
        print("substraction -total:",imaginary,"+","i",realpart,sep="")

    def multiplication(self,c1,c2):
        real=(c1.x*c2.x)-(c1.y*c2.y)
        print("realll",real)
        imaginary=str((c1.x*c2.y)+(c2.x*c1.y))
        print("imaginary:"+"i"+str(imaginary))
        #print(":",str(real),"+",imaginary)
        print("output mul",real,"+","i",imaginary,sep="")
        
        
    def division(self,c1,c2):
        print("division")
        pass
        #first_part=(((c1.x)*(c2.x))-((c1.y*c2.y)))/(((c2.x*c2.x)-(c2.y*c2.y)))
        #second_part=(((str((c1.y)*str(c2.x)))+"i")-((str(c1.x))*(c2.y)+"i"))/(((c2.x*c2.x)-(c2.y*c2.y)))
        #division_result=first_part/second_part
        #print("firsttparttt",first_part)

        #print("secondparttt",second_part)
       # print("division_result:",division_result)


c1=Complex()
c2=Complex()
c3=Complex()
print("first")
c1.initComplex()
c1.display()
print("sedcondddddd")
c2.initComplex()
c2.display()
c3.addition(c1,c2)
c3.substraction(c1,c2)
c3.multiplication(c1,c2)
c3.division(c1,c2)
















        


