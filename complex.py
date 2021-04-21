class Complex:
    def __init__(self):
        self.x = 0
        self.y= 0
        self.p = 0 
        self.q = 0            
    def __str__ (self,x,y,p,q):
        self.x=x
        self.y=y
        self.p=p
        self.q=q
        print("first complex numebrrrr",self.x,"+",self.y,"i", sep="")
        print("second complex number:",self.p,"+",self.q,"i", sep="")

    def addition(self,x,y,p,q):
        imaginary=x+p
        realpart=y+q
        
        print("addition-total:",imaginary,"+","i",realpart,sep="")
    
    def substraction(self,x,y,p,q):
        imaginary=x-p
        realpart=y-q
               
        print("substraction total:",imaginary,"+",realpart,"i",sep="")

    def multiplication(self,x,y,p,q):
        real=(x*p)-(y*q)
        print("realll",real)
        imaginary=str((x*q)+(p*y))
        print("imaginary:"+"i"+str(imaginary))
        #print(":",str(real),"+",imaginary)
        print("output multiplication:",real,"+","i",imaginary,sep="")
        
        
    def division(self,x,y,p,q):
        print("division")
        
        first_part=(((x)*(p))-((y*q)))/(((p*p)-(q*q)))
        second_part=((((y)*(str(p)))+"i")-((x)*(q)+"i"))/((p*p)-(q*q))
        division_result=first_part/second_part
        print("firsttparttt",first_part)

        print("secondparttt",second_part)
        print("division_result:",division_result)
