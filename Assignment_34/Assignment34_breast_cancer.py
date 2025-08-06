"""####################################################################
    
Output:
['mean radius' 'mean texture' 'mean perimeter' 'mean area'
 'mean smoothness' 'mean compactness' 'mean concavity'
 'mean concave points' 'mean symmetry' 'mean fractal dimension'
 'radius error' 'texture error' 'perimeter error' 'area error'
 'smoothness error' 'compactness error' 'concavity error'
 'concave points error' 'symmetry error' 'fractal dimension error'
 'worst radius' 'worst texture' 'worst perimeter' 'worst area'
 'worst smoothness' 'worst compactness' 'worst concavity'
 'worst concave points' 'worst symmetry' 'worst fractal dimension']
mean radius                0
mean texture               0
mean perimeter             0
mean area                  0
mean smoothness            0
mean compactness           0
mean concavity             0
mean concave points        0
mean symmetry              0
mean fractal dimension     0
radius error               0
texture error              0
perimeter error            0
area error                 0
smoothness error           0
compactness error          0
concavity error            0
concave points error       0
symmetry error             0
fractal dimension error    0
worst radius               0
worst texture              0
worst perimeter            0
worst area                 0
worst smoothness           0
worst compactness          0
worst concavity            0
worst concave points       0
worst symmetry             0
worst fractal dimension    0
target                     0
dtype: int64
Accuracy is  96.49122807017544
Confusion Matrix
[[40  3]
 [ 1 70]]
Classification Report                precision    recall  f1-score   support

           0       0.98      0.93      0.95        43
           1       0.96      0.99      0.97        71

    accuracy                           0.96       114
   macro avg       0.97      0.96      0.96       114
weighted avg       0.97      0.96      0.96       114

ROC-AUC score: 0.9580740255486406
Precision: 0.958904109589041
Recall Score : 0.9859154929577465
F1 Score : 0.9722222222222222

####################################################################"""
import pandas as pd # Loading 
import numpy as np
  
from sklearn.datasets import load_breast_cancer
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,roc_auc_score,precision_score,recall_score,f1_score # aquarety


def CancerPredition():

    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)

    df['target'] = data.target
    # print(data.feature_names)

    print(df.isnull().sum())  

    x=df.drop(columns='target')
    y=df['target']

    sc=StandardScaler()
    xscaler=sc.fit_transform(x)

    x_train,x_test,y_train,y_test=train_test_split(xscaler,y,test_size=0.2,random_state=42)
    model=RandomForestClassifier(random_state=42)
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)

    accuracy=accuracy_score(y_test,y_pred)
    print("Accuracy is ",accuracy*100)

    CM=confusion_matrix(y_test,y_pred)
    print("Confusion Matrix")
    print(CM)

    CL=classification_report(y_test,y_pred)
    print("Classification Report ",CL)

    ROC_AUC = roc_auc_score(y_test, y_pred)
    print("ROC-AUC score:", ROC_AUC)

    pre= precision_score(y_test, y_pred)
    print("Precision:", pre)

    RS = recall_score(y_test, y_pred)
    print("Recall Score :",RS)

    f1 = f1_score(y_test, y_pred)
    print("F1 Score :",f1)

    importance=pd.Series(model.feature_importances_, index=data.feature_names)
    importance=importance.sort_values(ascending=True)

    plt.figure(figsize=(10, 8))
    importance.plot(kind='barh', color='skyblue')
    plt.title("Feature Importances from Breast cancer ")
    plt.xlabel("Importance Score")
    plt.tight_layout()
    plt.show()


def main():
    CancerPredition()

if __name__=="__main__":
    main()