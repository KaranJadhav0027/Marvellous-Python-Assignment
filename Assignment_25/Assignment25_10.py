"""############################################################
OutPut:
 DataFrame:
   Age  Salary  Purchased
0   25   50000          1
1   30   60000          0
2   45   80000          1
3   35   65000          0
4   22   45000          1

x_train:
   Age  Salary
4   22   45000
2   45   80000
0   25   50000
3   35   65000

x_test:
   Age  Salary
1   30   60000

y_train:
4    1
2    1
0    1
3    0
Name: Purchased, dtype: int64

y_test:
1    0
Name: Purchased, dtype: int64

###############################################################"""

import pandas as pd
from sklearn.model_selection import train_test_split  

def operation():
    data={'Age':[25,30,45,35,22],'Salary':[50000,60000,80000,65000,45000],'Purchased':[1,0,1,0,1]}
    df = pd.DataFrame(data)
    
    print(" DataFrame:")
    print(df)
    
    X = df[['Age', 'Salary']]
    Y = df['Purchased']

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("x_train:")
    print(x_train)
    print("x_test:")
    print(x_test)
    print("y_train:")
    print(y_train)
    print("y_test:")
    print(y_test)
  
def main():
    operation()
    
if __name__=="__main__":
    main()