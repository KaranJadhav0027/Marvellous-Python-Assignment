"""####################################################################
    
Output:
Index(['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu',
       'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime',
       'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery',
       'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc',
       'Walc', 'health', 'absences', 'G1', 'G2', 'G3'],
      dtype='object')

Shape: (395, 33)

2370.000000000001
1615.735480370607
1323.7731945473881
1144.7867141762877
986.4386353940158
851.3280438840436
759.9619401009313
683.2160610039816
628.5179924871038

####################################################################"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def Student():
    df= pd.read_csv("student-mat-clean.csv")
    df.dropna(inplace=True)
    
    # categorical_cols = df.select_dtypes(include='object').columns

     # One-hot encoding
    print(df.columns)
    print("Shape:", df.shape)
    DF = pd.get_dummies(df, drop_first=True)

    # print("Missing Values in each column ",DF.isnull().sum())

    # X = df['failures','studytime','absences', 'G1', 'G2', 'G3']
    features = ['failures', 'studytime', 'absences', 'G1', 'G2', 'G3']
    X = DF[features]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    WCSS=[]
    for k in range(1,10):
        model=KMeans(n_clusters=k,init='k-means++',n_init=10,random_state=42)
        model.fit(X_scaled)
        print(model.inertia_) #WCSS(innershiya)
        WCSS.append(model.inertia_)

    plt.plot(range(1,10),WCSS,marker='o')
    plt.title("Elobw method foe k Mean")
    plt.xlabel("Value of K")
    plt.ylabel("With in Cluster Sum of Square (WCSS)")
    plt.grid(True)
    plt.show()

    
    model = KMeans(n_clusters=3, init='k-means++', n_init=10, random_state=42)
    y_kmeans = model.fit_predict(X_scaled)

    # Visualize only 2D for plotting (use first two features for simplicity)
    plt.figure(figsize=(8, 6))
    plt.scatter(X_scaled[y_kmeans == 0, 0], X_scaled[y_kmeans == 0, 1], s=100, c='red', label='Cluster 0')
    plt.scatter(X_scaled[y_kmeans == 1, 0], X_scaled[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 1')
    plt.scatter(X_scaled[y_kmeans == 2, 0], X_scaled[y_kmeans == 2, 1], s=100, c='green', label='Cluster 2')

    # Plot centroids
    plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids', marker='X')

    plt.title("KMeans Clustering in Student Data")
    plt.xlabel("Feature 1 (scaled)")
    plt.ylabel("Feature 2 (scaled)")
    plt.legend()
    plt.grid(True)
    plt.show()

   

def main():
    Student()

if __name__=="__main__":
    main()