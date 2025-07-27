import pandas as pd # Loading 
import numpy as np
from sklearn.model_selection import train_test_split # trsin and test
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix # aquarety

def WinePredictor(Datapath):
    df=pd.read_csv(Datapath)

    df.dropna(inplace=True)

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
   
    print("Final best Accuracy is :",accuracy*100)
    cm=confusion_matrix(y_test,y_pred)
    print(cm)

def main():
    WinePredictor("WinePredictor.csv")

if __name__=="__main__":
    main()