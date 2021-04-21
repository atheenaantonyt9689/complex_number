from complex import Complex


def run():
    x=int(input("enter the first_real part:"))
    y=int(input("enter the first_imaginary part:"))
    p=int(input("enter the second_real part:"))
    q=int(input("enter the second_imaginary part:"))

    obj1=Complex() 
    obj2=Complex()
    obj3=Complex()
    
    c1=obj1.__str__(x,y,p,q)
    obj1.addition(x,y,p,q)
    obj1.substraction(x,y,p,q)
    obj1.multiplication(x,y,p,q)
    obj1.division(x,y,p,q)
    

    

run()
