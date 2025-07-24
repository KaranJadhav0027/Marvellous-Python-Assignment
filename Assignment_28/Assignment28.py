"""####################################################################
    
Output:
    Missing Values in each column  Class                           0
Alcohol                         0
Malic acid                      0
Ash                             0
Alcalinity of ash               0
Magnesium                       0
Total phenols                   0
Flavanoids                      0
Nonflavanoid phenols            0
Proanthocyanins                 0
Color intensity                 0
Hue                             0
OD280/OD315 of diluted wines    0
Proline                         0
dtype: int64

Best Value of K is : 12

Final best Accuracy is : 97.22222222222221

Confusion Matrix
[[14  0  0]
 [ 1 13  0]
 [ 0  0  8]]

####################################################################"""


import pandas as pd # Loading 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split # trsin and test
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix # aquarety


def WinePredictor(Datapath):
    df=pd.read_csv(Datapath)

    df.dropna(inplace=True)

    print("Missing Values in each column ",df.isnull().sum())

    x=df.drop(columns=['Class'])
    y=df['Class']
 
    scaler=StandardScaler()
    x_scale=scaler.fit_transform(x)

    x_train,x_test,y_train,y_test=train_test_split(x_scale,y,test_size=0.2,random_state=42)
 
    accuracy_scores=[]
    k_range =range(1,18)

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


def main():
    WinePredictor("WinePredictor.csv")

if __name__=="__main__":
    main()