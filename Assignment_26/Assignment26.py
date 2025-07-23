"""####################################################################
    
Output:
         Unnamed: 0
count   30.000000
mean    15.500000
std      8.803408
min      1.000000
25%      8.250000
50%     15.500000
75%     22.750000
max     30.000000
(30, 4)
Best Value of K is : 5
Final best Accuracy is : 100.0
[[1 0]
 [0 5]]

####################################################################"""
import pandas as pd # Loading 
import numpy as np

from matplotlib.pyplot import figure,show  # vigulation
import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split # trsin and test
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix # aquarety


def PlayPredictor(Datapath):
    df=pd.read_csv(Datapath)

    print(df.describe())
    print(df.shape)
    df.drop(columns=['Unnamed: 0'],inplace=True)
    
    # encoding_maps = {
    # 'Whether': {'Sunny': 0, 'Overcast': 1, 'Rainy': 2},
    # 'Temperature': {'Hot': 0, 'Mild': 1, 'Cool': 2},
    # 'Play': {'No': 0, 'Yes': 1}
    # }
    # for column, mapping in encoding_maps.items():
    #   df[column] = df[column].map(mapping)
    
    df['Whether']=df['Whether'].map({'Sunny': 0, 'Overcast': 1, 'Rainy': 2})
    df['Temperature']=df['Temperature'].map({'Hot': 0, 'Mild': 1, 'Cool': 2})
    df['Play']=df['Play'].map({'No': 0, 'Yes': 1})
    
    # df["variety"]=df["variety"].map({"Setosa":0,"Versicolor":1,"Virginica":2})

    df.dropna(inplace=True)
    
    x=df.drop(columns=['Play'])
    y=df['Play']
 
    scaler=StandardScaler()
    x_scale=scaler.fit_transform(x)

    x_train,x_test,y_train,y_test=train_test_split(x_scale,y,test_size=0.2,random_state=42)
    
    # for Single Chaking 
    # model=KNeighborsClassifier(n_neighbors=3)
    # model.fit(x_train,y_train)
    # y_pred=model.predict(x_test)

    # accuracy=accuracy_score(y_test,y_pred)

    # print("Accuracy Score is :",accuracy)
    accuracy_scores=[]
    k_range =range(1,18)
 
    #  Multiple Value Chacking
    for k in k_range:
        model=KNeighborsClassifier(n_neighbors=k)
        model.fit(x_train,y_train)
        y_pred=model.predict(x_test)
        accuracy=accuracy_score(y_test,y_pred)
        accuracy_scores.append(accuracy)
    
    # TO Show the Value of Accuracy 
    plt.figure(figsize=(8,5))
    plt.plot(k_range,accuracy_scores,marker='o',linestyle='--')
    plt.title("Accuracy vs k Value")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy of model")
    plt.grid(True)
    plt.xticks(k_range)
    plt.show()

    best_k=k_range[accuracy_scores.index(max(accuracy_scores))]
    print("Best Value of K is :",best_k)
   
    model=KNeighborsClassifier(n_neighbors=best_k)
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    accuracy=accuracy_score(y_test,y_pred)
   
    print("Final best Accuracy is :",accuracy*100)
    cm=confusion_matrix(y_test,y_pred)
    print(cm)

def main():
    PlayPredictor("PlayPredictor.csv")

if __name__=="__main__":
    main()