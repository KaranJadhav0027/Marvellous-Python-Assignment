"""####################################################################
    
Output:
Index(['title', 'text', 'subject', 'date', 'label'], dtype='object')
Shape: (44898, 5)
Missing Values in each column  title      0
text       0
subject    0
date       0
label      0
dtype: int64
Accuracy:  98.4966592427617
Confusion Matrix:
[[4624   86]
 [  49 4221]]
Classification Report:
               precision    recall  f1-score   support

           0       0.99      0.98      0.99      4710
           1       0.98      0.99      0.98      4270

    accuracy                           0.98      8980
   macro avg       0.98      0.99      0.98      8980
weighted avg       0.99      0.98      0.98      8980

####################################################################"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def NEWS():
    fake = pd.read_csv("Fake.csv")
    real = pd.read_csv("True.csv")

    fake['label'] = 0
    real['label'] = 1

    df = pd.concat([fake, real], axis=0)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    print(df.columns)
 
    print("Shape:", df.shape)
    # print(df.head())

    print("Missing Values in each column ",df.isnull().sum())

    X = df['text']
    Y = df['label']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=500)
    model.fit(X_train_tfidf, Y_train)

    y_pred = model.predict(X_test_tfidf)

    accuracy = accuracy_score(Y_test, y_pred)
    print("Accuracy: ",accuracy*100)
    cm=confusion_matrix(Y_test, y_pred)
    print("Confusion Matrix: ")
    print(cm)

    print("Classification Report:\n", classification_report(Y_test, y_pred))

    plt.figure(figsize=(6,4))
    sns.countplot(x='label', data=df, palette='Set2')
    plt.title("Distribution of Fake vs Real News")
    plt.xticks([0, 1], ['Fake', 'Real'])
    plt.show()

    ############################## OR ###################################
    # label_counts = df['label'].value_counts().sort_index()  # Assumes 0=Fake, 1=Real
    # x = ['Fake', 'Real']
    # y = label_counts.values

    # plt.figure(figsize=(6, 4))
    # plt.bar(x, y, color=['#66c2a5', '#fc8d62'])  # Matching 'Set2' colors
    # plt.title("Distribution of Fake vs Real News")
    # plt.xlabel("News Type")
    # plt.ylabel("Count")
    # plt.show()

def main():
    NEWS()

if __name__=="__main__":
    main()