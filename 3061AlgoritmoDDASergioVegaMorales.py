import matplotlib.pyplot as plt
import numpy as np

def algoritmoDDA(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs (y2 - y1)
    if (dx>dy):
        steps=(dx)
    else:
        steps=(dy)
         
         # There must be one equal to 1, and one less than 1
    xinc = float(dx / steps)
    yinc=  float(dy / steps)
         # Round off to ensure that the increment of x and y is less than or equal to 1, so that the generated straight line is as uniform as possible
    xinc = round (xinc, 1)
    yinc = round (yinc, 1)
    
    for i in range(1, int(steps + 1)):
		 # Draw pixels
        plt.scatter(round (x1), round(y1))
        plt.plot(round(x1),round(y1))
        x1 = (x1+xinc)
        y1 = (y1+yinc)
        print("("+str(round(x1))+", "+str(round(y1))+")")
        
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Digital Differential Analyzer')
    plt.show()
if __name__ == "__main__":
    x1 = int(input("Ingrese el valor para X1= "))
    y1 = int(input("Ingrese el valor para Y1= "))
    x2 = int(input("Ingrese el valor para X2= "))
    y2 = int(input("Ingrese el valor para Y2= "))
    
   
    algoritmoDDA(x1, y1, x2, y2)


