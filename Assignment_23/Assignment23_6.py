"""############################################################

  
Output:
Dataset loade succesfully
    Name  Math  Science  English  Total
0   Amit    85       92       75    252
1  Sagar    90       88       85    263
2  Pooja    78       80       82    240


Data Sorted :
    Name  Math  Science  English  Total
1  Sagar    90       88       85    263
0   Amit    85       92       75    252
2  Pooja    78       80       82    240

###############################################################"""

import pandas as pd
import matplotlib.pyplot as plt

def operation():
    df=pd.read_csv("Student2.csv")
    
    print("Dataset loade succesfully")
    print(df)
    order = df.sort_values(by="Total", ascending=False)
    
    print("Data Sorted :")
    print(order)

def main():
    operation()
    
if __name__=="__main__":
    main()