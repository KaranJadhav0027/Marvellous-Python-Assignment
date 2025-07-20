"""############################################################
Output:
Dataset loade succesfully
    Name  Math  Science  English
0   Amit    85       92       75
1  Sagar    90       88       85
2  Pooja    78       80       82

Normalized Math Scores (Min-Max):
   Math  Normalize
0    85   0.583333
1    90   1.000000
2    78   0.000000

###############################################################"""

import pandas as pd
import matplotlib.pyplot as plt

def operation():
    df=pd.read_csv("StudentMarks.csv")
    
    print("Dataset loade succesfully")
    print(df)
    
    df['Normalize'] = (df['Math'] - df['Math'].min()) / (df['Math'].max() - df['Math'].min())

    print("\nNormalized Math Scores (Min-Max):")
    print(df[['Math', 'Normalize']])

def main():
    operation()
    
if __name__=="__main__":
    main()