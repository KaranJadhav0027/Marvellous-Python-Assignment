"""############################################################
OutPut:
 DataFrame:
   Age  Purchased
0   22          0
1   25          1
2   47          1
3   52          0
4   46          1
5   56          0
X_train:
   Age
5   56
2   47
4   46
3   52
y_train:
5    0
2    1
4    1
3    0
Name: Purchased, dtype: int64
X_test:
   Age
0   22
1   25
y_test:
0    0
1    1
Name: Purchased, dtype: int64

###############################################################"""

import pandas as pd
from sklearn.model_selection import train_test_split

def operation():
    data={'Age':[22,25,47,52,46,56],'Purchased':[0,1,1,0,1,0]}
    df = pd.DataFrame(data)
    
    print(" DataFrame:")
    print(df)
    
    X = df[['Age']]         
    Y = df['Purchased']    
    
   
    x_train, x_test, y_train, y_test = train_test_split(X, Y,test_size=0.20, random_state=42)
    
    print("X_train:")
    print(x_train)
    print("y_train:")
    print(y_train)
    print("X_test:")
    print(x_test)
    print("y_test:")
    print(y_test)
  
def main():
    operation()
    
if __name__=="__main__":
    main()