"""############################################################

  
Output:
Dataset loade succesfully
    Name  Math  Science
0   Amit   NaN     92.0
1  Sagar  90.0      NaN
2  Pooja  78.0     80.0

After Fill Missing Values with Column Averages:
    Name  Math  Science
0   Amit  84.0     92.0
1  Sagar  90.0     86.0
2  Pooja  78.0     80.0

###############################################################"""

import pandas as pd

def operation():
    df=pd.read_csv("MissingValue.csv")
    
    print("Dataset loade succesfully")
    print(df)

    df = df.fillna(df.mean(numeric_only=True))

    print("After Fill Missing Values with Column Averages:")
    print(df)
     
def main():
    operation()
    
if __name__=="__main__":
    main()