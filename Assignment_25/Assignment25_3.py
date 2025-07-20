"""############################################################
OutPut:
DataFrame:
     City
0    Pune
1  Mumbai
2   Delhi
3    Pune
4   Delhi

Encoded DataFrame:
     City  City_encoded
0    Pune             2
1  Mumbai             1
2   Delhi             0
3    Pune             2
4   Delhi             0

###############################################################"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def operation():
    data={'City':['Pune','Mumbai','Delhi','Pune','Delhi']}
    df = pd.DataFrame(data)
    
    print(" DataFrame:")
    print(df)
    
    le = LabelEncoder()
    df['City_encoded'] = le.fit_transform(df['City'])
    
    print("Encoded DataFrame:")
    print(df)
  
def main():
    operation()
    
if __name__=="__main__":
    main()