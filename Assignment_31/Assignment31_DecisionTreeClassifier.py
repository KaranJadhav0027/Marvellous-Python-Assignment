"""####################################################################
    
Output:
Accurcy is : 95.0
Confusion Matrix:
 [[84  5]
 [ 2 49]]
Classification Report:
               precision    recall  f1-score   support

           2       0.98      0.94      0.96        89
           4       0.91      0.96      0.93        51

    accuracy                           0.95       140
   macro avg       0.94      0.95      0.95       140
weighted avg       0.95      0.95      0.95       140

ROC-AUC score: 0.9523022692222958
####################################################################"""
import pandas as pd # Loading 
import numpy as np

from matplotlib.pyplot import figure,show  # vigulation
import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split # trsin and test
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,roc_auc_score  # aquarety


def CancerPredition(Datapath):
  df = pd.read_csv(Datapath)
  
  df.dropna(inplace=True)
    
  # One-hot encoding
  DF = pd.get_dummies(df, drop_first=True)

#   print("Shape before encoding: ",df.shape)
#   print("Shape after encoding: ",DF.shape)

  X = DF.drop('CancerType', axis=1)
  Y = DF['CancerType']

  X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

  model= DecisionTreeClassifier()

  model.fit(X_train,Y_train)

  y_pred=model.predict(X_test)

  accuracy=accuracy_score(Y_test,y_pred)

  print("Accurcy is :",accuracy*100)
 
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
    CancerPredition("breast-cancer-wisconsin.csv")

if __name__=="__main__":
    main()