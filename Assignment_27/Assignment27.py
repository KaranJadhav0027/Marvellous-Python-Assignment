"""####################################################################
    
Output:
Clean the dataset
Missing Values in each column  TV           0
radio        0
newspaper    0
sales        0
dtype: int64

Correalation Matrix
                 TV     radio  newspaper     sales
TV         1.000000  0.054809   0.056648  0.782224
radio      0.054809  1.000000   0.354104  0.576223
newspaper  0.056648  0.354104   1.000000  0.228299
sales      0.782224  0.576223   0.228299  1.000000

Mean Square Error : 1.3890870234899657

Root mean Square Error is : 1.1785953603718138

R Square Value : 0.8721004816045135

model Coefficient are :
TV:0.043594980013716034
radio:0.19927632341597368
newspaper:0.014663100417474817
Y Intercept is  2.5791155256527336

####################################################################"""
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def MarvellousAdvertise(Datapath):
    df=pd.read_csv(Datapath)
   
    print("Clean the dataset ")
    df.drop(columns=['Unnamed: 0'],inplace=True)

    print("Missing Values in each column ",df.isnull().sum())

    print("Correalation Matrix") #multiple indepenedn veriable compare to dependent variables
    print(df.corr())

    x=df[['TV','radio','newspaper']]
    y=df['sales']

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5,random_state=42)

    model=LinearRegression()
    model.fit(x_train,y_train)

    y_pred=model.predict(x_test)

    MSE=metrics.mean_absolute_error(y_test,y_pred)
    RMSE=np.sqrt(MSE)
    r2=metrics.r2_score(y_test,y_pred)

    print("Mean Square Error :",MSE)
    print("Root mean Square Error is :",RMSE) 
    print("R Square Value :",r2) 

    print("model Coefficient are :")
    for col,coef in zip(x.columns,model.coef_):
        print(f"{col}:{coef}")
    
    print("Y Intercept is ",model.intercept_)
    
def main():
    MarvellousAdvertise("Advertising.csv")

if __name__=="__main__":
    main()
