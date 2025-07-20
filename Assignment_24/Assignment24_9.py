"""############################################################
Output:
Dataset loade succesfully
    Name  Math  Science  English  Total
0   Amit    85       92       75    252
1  Sagar    90       88       85    263
2  Pooja    78       80       82    240
Dataset loaded successfully
    Name  Mathematics  Science  English  Total
0   Amit           85       92       75    252
1  Sagar           90       88       85    263
2  Pooja           78       80       82    240

###############################################################"""

import pandas as pd

def operation():
    df=pd.read_csv("Student2.csv")
    
    print("Dataset loade succesfully")
    print(df)

    df.rename(columns={"Math": "Mathematics"}, inplace=True)
    
    print("Dataset loaded successfully")
    print(df)
   
    
def main():
    operation()
    
if __name__=="__main__":
    main()