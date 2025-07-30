"""####################################################################
    
Output:
Shape before encoding:  (45211, 17)
Shape after encoding:  (45211, 43)
Best Value of K is : 22
Final best Accuracy is : 88.42198385491541
Confusion Matrix:
 [[7739  213]
 [ 837  254]]
Classification Report:
               precision    recall  f1-score   support

       False       0.90      0.97      0.94      7952
        True       0.54      0.23      0.33      1091

    accuracy                           0.88      9043
   macro avg       0.72      0.60      0.63      9043
weighted avg       0.86      0.88      0.86      9043

ROC-AUC score: 0.8238774420122937

####################################################################"""

import pandas as pd # Loading 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split # trsin and test
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,roc_auc_score # aquarety

def BankFull(): 
  df = pd.read_csv('bank-full-clean.csv')
  
  df.dropna(inplace=True)
    
  categorical_cols = df.select_dtypes(include='object').columns

  # One-hot encoding
  DF = pd.get_dummies(df, drop_first=True)

  print("Shape before encoding: ",df.shape)
  print("Shape after encoding: ",DF.shape)

  X = DF.drop('y_yes', axis=1)
  Y = DF['y_yes']

  X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

  accuracy_scores=[]
  k_range =range(1,18)
 
    #  Multiple Value Chacking
  for k in k_range:
      model=KNeighborsClassifier(n_neighbors=k)
      model.fit(X_train,Y_train)
      y_pred=model.predict(X_test)
      accuracy=accuracy_score(Y_test,y_pred)
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
  model.fit(X_train,Y_train)
  y_pred=model.predict(X_test)
  accuracy=accuracy_score(Y_test,y_pred)
  
  print("Final best Accuracy is :",accuracy*100)

  cm = confusion_matrix(Y_test, y_pred)
  print("Confusion Matrix:\n", cm)

  print("Classification Report:\n", classification_report(Y_test, y_pred))

  y_prob = model.predict_proba(X_test)[:, 1]
  ROC_AUC = roc_auc_score(Y_test, y_prob)
  print("ROC-AUC score:", ROC_AUC)

  importance=pd.Series(model.feature_importances_,index=X.columns)
  importance=importance.sort_values(ascending=False)

  importance.plot(kind='bar',figsize=(10,6),title="Feture Importance")
  plt.show()

def main():
    BankFull()

if __name__=="__main__":
   main()
