from complex import Complex


def run():
    x=int(input("enter the first_real part:"))
    y=int(input("enter the first_imaginary part:"))
    p=int(input("enter the second_real part:"))
    q=int(input("enter the second_imaginary part:"))

    obj1=Complex(x,y) 
    obj1.display()
    obj2=Complex(p,q)
    obj1.addition(obj2)
    obj1.substraction(obj2)
    obj1.multiplication(obj2)
    obj1.division(obj2)


    
    

    

run()
