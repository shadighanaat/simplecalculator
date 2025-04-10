while True:  
    operation=input('enter the operation:')
    num1=int(input('enter a number1:'))
    num2=int(input('enter a number2:'))

    if operation=='+':
        def  jam(a,b):

            return a+b
        print(jam(num1,num2))
    if operation=='-':
        def menha(a,b):
            
            return a-b
        print(menha(num1,num2))
    if operation=='*':
        def zarb(a,b):
           
            return a*b
        print(zarb(num1,num2))
    if operation=='/':
        def taghsim(a,b):
                if b==0:
                        return False
                else:
                    return a/b
        print(taghsim(num1,num2))
    if operation=='**':
        def tavan(a,b):
            
            return a**b
        print(tavan(num1,num2))
