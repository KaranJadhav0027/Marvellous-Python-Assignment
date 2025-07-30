"""####################################################################
    
Output:

######################## K NEIGHBORS CLASSIFICATION ################################
Missing Values in each column  Pregnancies                 0
Glucose                     0
BloodPressure               0
SkinThickness               0
Insulin                     0
BMI                         0
DiabetesPedigreeFunction    0
Age                         0
Outcome                     0
dtype: int64
Best Value of K is : 18
Final best Accuracy is : 76.62337662337663
Confusion Matrix
[[89 10]
 [26 29]]

######################## LINEAR REGRESSION ################################
Mean Square Error : 0.34812825999928243
Root mean Square Error is : 0.5900239486658846
R Square Value : 0.25500281176741757
model Coefficient are :
Pregnancies:0.03525037514851352
Glucose:0.18000137525812965
BloodPressure:-0.044122421138941256
SkinThickness:0.008482541809435577
Insulin:-0.03203368193253362
BMI:0.11848983624437341
DiabetesPedigreeFunction:0.036840487600210595
Age:0.07592475786332842
Y Intercept is  0.3520308567199474
  
####################################################################"""

import pandas as pd # Loading 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split # trsin and test
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.metrics import accuracy_score,confusion_matrix # aquarety


def DiabetesCase(Datapath):
    df=pd.read_csv(Datapath)

    # print("Dataset sample is :")
    # print(df.head(5))

    # print("Statistical Summary :")
    # print(df.describe)

    print("Correalation Matrix") #multiplr indepenedn veriable compare to dependent variables
    print(df.corr())

    plt.figure(figsize=(10,5))
    sns.heatmap(df.corr(),annot=True,cmap='coolwarm')
    plt.title("Marvellous Correaltion Heatmap")
    plt.show()

    df.dropna(inplace=True)

    print("Missing Values in each column ",df.isnull().sum())

    x=df.drop(columns=['Outcome'])
    y=df['Outcome']
 
    scaler=StandardScaler()
    x_scale=scaler.fit_transform(x)

    x_train,x_test,y_train,y_test=train_test_split(x_scale,y,test_size=0.2,random_state=42)
 
######################## K NEIGHBORS CLASSIFICATION ################################
    accuracy_scores=[]
    k_range =range(1,25)

    for k in k_range:
        model=KNeighborsClassifier(n_neighbors=k)
        model.fit(x_train,y_train)
        y_pred=model.predict(x_test)
        accuracy=accuracy_score(y_test,y_pred)
        accuracy_scores.append(accuracy)
    
    best_k=k_range[accuracy_scores.index(max(accuracy_scores))]
    print("Best Value of K is :",best_k)
   
    model=KNeighborsClassifier(n_neighbors=best_k)
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    accuracy=accuracy_score(y_test,y_pred)

    plt.figure(figsize=(8,5))
    plt.plot(k_range,accuracy_scores,marker='o',linestyle='--')
    plt.title("Accuracy vs k Value")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy of model")
    plt.grid(True)
    plt.xticks(k_range)
    plt.show()
   
    print("Final best Accuracy is :",accuracy*100)
    cm=confusion_matrix(y_test,y_pred)
    print("Confusion Matrix")
    print(cm)


######################## LINEAR REGRESSION ################################
    LModel=LinearRegression().fit(x_train,y_train)

    Lpred=LModel.predict(x_test)

    MSE=metrics.mean_absolute_error(y_test,Lpred)
    RMSE=np.sqrt(MSE)
    r2=metrics.r2_score(y_test,Lpred)

    print("Mean Square Error :",MSE)
    print("Root mean Square Error is :",RMSE) 
    print("R Square Value :",r2) 

    print("model Coefficient are :")
    for col,coef in zip(x.columns,LModel.coef_):
        print(f"{col}:{coef}")
    
    print("Y Intercept is ",LModel.intercept_)
    

def main():
    DiabetesCase("diabetes.csv")

if __name__=="__main__":
    main()

"""
Summary of Your Code

1. Libraries Import
You use important libraries like pandas, numpy, matplotlib, seaborn, and sklearn for data handling, visualization, and modeling.

2. Data Loading & Cleaning
Loads data from a CSV file (diabetes.csv).

Removes missing data using dropna() (though your dataset already has zero missing values).

Displays the count of missing values in each column.

3. Feature Selection & Scaling
Separates features (x) and target (y).

Uses StandardScaler to normalize the feature values (important for KNN).

4. K-Nearest Neighbors (KNN) Classifier
Trains the model with different k values from 1 to 24.

Finds the best k based on accuracy.

Displays the confusion matrix and accuracy.

Plots Accuracy vs. K graph.

5. Linear Regression
Trains a linear regression model on the same data.

Calculates and prints metrics like:

Mean Absolute Error (MAE)

Root Mean Square Error (RMSE)

R² score

Prints model coefficients and intercept.
"""