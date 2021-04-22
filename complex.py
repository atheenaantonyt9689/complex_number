class Complex:
    def __init__(self,x,y):
        self.x = x
        self.y= y
              
    def display(self):
       
        print("first complex numebrrrr",self.x,"+",self.y,"i", sep="")        

    def addition(self,obj2): 
        
        sum_real=self.x + obj2.x
        sum_complex=self.y + obj2.y        
        print("addition:",sum_real,"+",sum_complex,"i", sep="")     
    
    def substraction(self,obj2): 
        
        sub_real=self.x -obj2.x
        sub_complex=self.y - obj2.y        
        print("substracvtion:",sub_real,"+",sub_complex,"i", sep="")     
    

    def multiplication(self,obj2):
        real=(self.x*obj2.x)-(self.x*obj2.x)
        imaginary=((self.x*obj2.y)+(obj2.x*self.x))
        print("multiplication result:",real,"+",imaginary,"i", sep="") 
        
        
    """def division(self,obj2):
        print("division")
        
        first_part=(((self.x)*(obj2.x))-((self.y*obj2.y)))/(((obj2.x*obj2.x)-(obj2.x*obj2.x)))
        second_part=((((self.y)*(str(obj2.x)))+"i")-((self.x)*(obj2.y)+"i"))/(((obj2.x*obj2.x)-(obj2.x*obj2.x)))
        division_result=first_part/second_part
        
        print("division_result:",division_result)"""

