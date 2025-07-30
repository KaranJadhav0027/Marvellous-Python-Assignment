"""####################################################################
    
Output:

Shape before encoding: (45211, 17)
Shape after encoding: (45211, 43)
Accuracy Score : 89.4061705186332
Confusion Matrix:
 [[7881   71]
 [ 887  204]]
Classification Report:
               precision    recall  f1-score   support

       False       0.90      0.99      0.94      7952
        True       0.74      0.19      0.30      1091

    accuracy                           0.89      9043
   macro avg       0.82      0.59      0.62      9043
weighted avg       0.88      0.89      0.87      9043

ROC-AUC Score: 0.9187765225634283

####################################################################"""

import pandas as pd # Loading 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split # trsin and test
# from sklearn.neighbors import KNeighborsClassifier
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

  model=RandomForestClassifier(n_estimators=150,max_depth=10,random_state=42)

  model.fit(X_train,Y_train)
  y_pred=model.predict(X_test)

  print("Accuracy Score :",accuracy_score(y_pred,Y_test)*100)

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
