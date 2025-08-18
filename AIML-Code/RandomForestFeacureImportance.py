import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report,accuracy_score
import matplotlib.pyplot as plt

def main():
    df=pd.read_csv("Telco-Customer-Churn.csv")

    df.drop(['customerID','gender'],axis=1,inplace=True)

    for col in df.select_dtypes(include='object'):
        df[col]=LabelEncoder().fit_transform(df[col])
    
    # print(df.head)
    X=df.drop('Churn',axis=1)
    Y=df['Churn']

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

    model=RandomForestClassifier(n_estimators=150,max_depth=10,random_state=42)

    model.fit(X_train,Y_train)
    y_pred=model.predict(X_test)

    print("Accuracy Score :",accuracy_score(y_pred,Y_test)*100)

     #to check Feature impoetances
    importance=pd.Series(model.feature_importances_,index=X.columns)
    importance=importance.sort_values(ascending=False)

    importance.plot(kind='bar',figsize=(10,6),title="Feture Importance")
    plt.show()

if __name__=="__main__":
    main()