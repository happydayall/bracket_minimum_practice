import tensorflow
import matplotlib.pyplot as plt
import math
import numpy as np

def function(x):
    y = x ** 3 / 3 - x
    return y 
    
def bracket_minimum(f , x = 2.0, s = 1e-2 , k = 1.5):
    z = 0
    a , ya = x , f(x)
    b , yb = a + s , f(a + s)
    if(yb > ya):
        a , b = b , a
        ya , yb = yb , ya
        s = -s
    while(1):
        c , yc = b + s , f(b + s)
        temp_ab = b - a
        temp_bc = c - b
        temp_gap = abs(temp_bc) - abs(temp_ab)
        if(temp_gap > temp_ab) & (z > 3):
            fix_c = c - 1/2 * s
            c = fix_c
            yc = f(fix_c)
        if(yc > yb):
            x = np.arange(-2 , 2, 0.01)
            plt.plot(x , f(x) , '-y')
            plt.plot(a , ya , 'ro')
            plt.plot(b , yb , 'bo')
            plt.plot(c, yc , 'go')
            plt.xlabel('x \n %.2f %.2f' %(ya , yc))
            plt.ylabel('y')
            plt.title('disparity: %.2f  k: %.2f' %(abs(yc - ya) , k))
            plt.show()
            if(a < c):
                return a ,b, c
            else:
                return c , b, a
        a , ya , b , yb = b , yb , c , yc
        s *= k
        z += 1
        
        
a , b , c = bracket_minimum(function)

print(a ,function(a) , b , function(b), c , function(c))