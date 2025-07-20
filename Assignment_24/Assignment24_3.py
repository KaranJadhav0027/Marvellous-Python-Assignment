"""############################################################
Output:
Dataset loade succesfully
    Name  Math  Science  English  Total
0   Amit    85       92       75    252
1  Sagar    90       88       85    263
2  Pooja    78       80       82    240

Average marks by gender:
Gender
Female    263.0
Male      246.0
Name: Total, dtype: float64
###############################################################"""

import pandas as pd


def operation():
    df=pd.read_csv("Student2.csv")
    
    print("Dataset loade succesfully")
    print(df)
    
    df['Gender'] = df.index.map(lambda i: 'Male' if i % 2 == 0 else 'Female')
    
    #Marks=Total
    average = df.groupby('Gender')['Total'].mean()
    print("\nAverage marks by gender:")
    print(average)

    
def main():
    operation()
    
if __name__=="__main__":
    main()