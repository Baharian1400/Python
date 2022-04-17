#x**3-x*2+2


def func( x ): 
    return x**3-x**2+2
  

def derivFunc( x ): 
    return 3 * x**2 - 2 * x 
  

def newtonRaphson( x ): 
    h = func(x) / derivFunc(x) 
    for i in range(10): 
        h = func(x)/derivFunc(x) 
          
        # x(i+1) = x(i) - f(x) / f'(x) 
        x = x - h 
      
    print("The value of the root is : ", 
                             "%.4f"% x) 
  
x0 = -20
newtonRaphson(x0) 
input()
  
