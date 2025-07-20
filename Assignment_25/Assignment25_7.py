"""############################################################
OutPut:
 DataFrame:
   Age
0   18
1   22
2   25
3   30
4   35

   Age  Age_Normalized
0   18        0.000000
1   22        0.235294
2   25        0.411765
3   30        0.705882
4   35        1.000000

###############################################################"""

import pandas as pd

def operation():
    data={'Age':[18,22,25,30,35]}
    df = pd.DataFrame(data)
    
    print(" DataFrame:")
    print(df)
   
    df['Age_Normalized'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())
    
    print(df)

def main():
    operation()
    
if __name__=="__main__":
    main()