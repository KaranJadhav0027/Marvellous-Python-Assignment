import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt


def MarvellousHeadBrainLinear(Datapath):
    Line="*"*50
    df=pd.read_csv(Datapath)
    print(Line)
    print("First Fer records of the dataset are :")
    print(Line)
    print(df.head())
    print(Line)

    print("Statistical data of the dataset are :")
    print(Line)
    print(df.describe())
    print(Line)

    x=df[['Head Size(cm^3)']]
    y=df[['Brain Weight(grams)']]

    print("Independent variables are : Head Size")
    print("Dependent variables are : Brain Weight")

    print("Total record in dataset :",x.shape)

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

    print("Dimentions of Training dataset :",x_train.shape)
    print("Dimentions of Testing dataset :",x_test.shape)

    model=LinearRegression()
    model.fit(x_train,y_train)

    y_pred=model.predict(x_test)

    mse=mean_squared_error(y_test,y_pred)
    rmse=np.sqrt(mse)
    r2=r2_score(y_test,y_pred)

    print("Visual Representation ")

    plt.figure(figsize=(8,5))
    plt.scatter(x_test,y_test,color='blue',label='Actual')
    plt.plot(x_test.values.flatten(),y_pred,color='red',linewidth=2,label="Regression Line")
    plt.xlabel('Head Size(cm^3)')
    plt.ylabel('Brain Weight(grams)')
    plt.title("Marvellous Head Brain Regration")
    plt.legend()
    plt.grid(True)
    plt.show()

    print("Result of Case Study ")
    print("Slop of line (m) :",model.coef_[0])
    print("Intercept (c) :",model.intercept_)
    print("Mean Square Error is :",mse)
    print("Root mean Square Error is :",rmse) # 1 vait 0 changali
    print("R Square Value :",r2)           #  0 to 1  1 near is changali


def main():
    MarvellousHeadBrainLinear("MarvellousHeadBrain.csv")

if __name__=="__main__":
    main()