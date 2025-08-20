import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    #Loab the data
    X=[1,2,3,4,5]
    Y=[3,4,2,4,5]

    print("Values of Independent Variables :",X)
    print("Values of Dependent Variables :",Y)

    mean_X=np.mean(X)
    mean_Y=np.mean(Y)

    print("X_mean is :",mean_X)
    print("Y_mean is :",mean_Y)

    n=len(X)

    numerator=0
    denomenator=0

    #Y=mX+C
    for i in range(n):
        numerator=numerator+(X[i]-mean_X)*(Y[i]-mean_Y)
        denomenator=denomenator+(X[i]-mean_X)**2

    m=numerator/denomenator
    print("Slop of line is m is :",m)

    C=mean_Y-(m*mean_X)
    
    print("Y intercept of line is :",C)
    
    x=np.linspace(1,6,n)
    y=C+m*x

    plt.plot(x,y,color='g',label="Regression Line")
    plt.scatter(X,Y,color='r',label="Scatter plot")

    plt.xlabel("X: Independent variable")
    plt.ylabel("Y : Dependent variable")

    plt.legend()
    plt.show()

    
def main():
    MarvellousPredictor()

if __name__=="__main__":
    main()