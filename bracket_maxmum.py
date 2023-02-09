import tensorflow
import matplotlib.pyplot as plt
import math
import numpy as np

def function(x):
    y = x ** 3 / 3 - x
    return y 
    
def bracket_minimum(f , x = -2 , s = 1e-2 , k = 1.2):
    z = 0
    a , ya = x , f(x)
    b , yb = a + s , f(a + s)
    a_list = []
    ya_list = []
    b_list = []
    yb_list = []
    c_list = []
    yc_list = []
    z_list = []
    if(yb < ya):
        a , ya , b , yb = b , yb , a , ya
        s = -s
    while(1):
        c , yc = b + s , f(b + s)
        a_list.append(a)
        ya_list.append(ya)
        b_list.append(b)
        yb_list.append(yb)
        c_list.append(c)
        yc_list.append(yc)
        z_list.append(z)
        if(yc < yb):
            x = np.arange(-2 , 2, 0.01)
            plt.plot(x , f(x) , '-y')
            plt.plot(a , ya , 'ro')
            plt.plot(b , yb , 'bo')
            plt.plot(c , yc , 'go')
            plt.xlabel('x \n %.2f %.2f' %(a_list[-1] , ya_list[-1]))
            plt.show()
            if(a < c):
                return a ,b, c
            else:
                return c , b, a
        a , ya , b , yb = b , yb , c , yc
        s *= k
        z += 1
        
        
bracket_minimum(function)

#print(a ,function(a) , b , function(b), c , function(c))