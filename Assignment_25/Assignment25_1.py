"""############################################################
OutPut:
Outliers in Salary column:
   Salary
5  100000

###############################################################"""

import pandas as pd

def operation():
    data={'Salary':[25000,27000,29000,31000,50000,100000]}
    
    df = pd.DataFrame(data)
    
    Q1 = df['Salary'].quantile(0.25)
    Q3 = df['Salary'].quantile(0.75)
    IQR = Q3 - Q1

    MIN = Q1 - 1.5 * IQR
    MAX = Q3 + 1.5 * IQR
    
    outliers = df[(df['Salary'] < MIN) | (df['Salary'] > MAX)]
    
    print("Outliers in Salary column:")
    print(outliers)
def main():
    operation()
    
if __name__=="__main__":
    main()