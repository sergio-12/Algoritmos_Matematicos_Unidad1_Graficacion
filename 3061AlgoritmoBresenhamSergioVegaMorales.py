import matplotlib.pyplot as plt
import numpy as np

def algoritmoBresenham(x1, y1, x2, y2):
    x=x1
    y=y1
    dx = abs(x2 - x1)
    dy = abs (y2 - y1)
    p=2*dy-dx

    for s in range(x1, x2):
        plt.scatter(round(x), round(y))
        plt.plot(round(x), round(y))
        x+=1

        if (p>0):
            p=p+2*dy
        else:
            p=p+(2*dy)-(2*dx)
            y+=1
         
        print("("+str(round(x1))+", "+str(round(y1))+")")
        
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Bresenham')
    plt.show()

if __name__ == "__main__":
    x1 = int(input("Ingrese el valor para X1= "))
    y1 = int(input("Ingrese el valor para Y1= "))
    x2 = int(input("Ingrese el valor para X2= "))
    y2 = int(input("Ingrese el valor para Y2= "))
    
    algoritmoBresenham(x1, y1, x2, y2)


