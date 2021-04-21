from test_complex import Complex
def run():
    x=int(input("enter the first_real part:"))
    y=int(input("enter the first_imaginary part:"))
    
    obj1=Complex() 
    c1=obj1.display(x,y)
    obj1.addition()

def run_sec():
    x=int(input("enter the second_real part:"))
    y=int(input("enter the second_imaginary part:"))

   obj2=Complex()
   c2=obj2.display(x,y)
   obj2.addition()
    


    
#common_obj=Complex()

run()
run_sec()