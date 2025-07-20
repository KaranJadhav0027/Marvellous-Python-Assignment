"""############################################################
Output:
Dataset loade succesfully
    Name  Math  Science  English
0   Amit    85       92       75
1  Sagar    90       88       85
2  Pooja    78       80       82
    Name  Math  Science  English  Gender_Female  Gender_Male
0   Amit    85       92       75          False         True
1  Sagar    90       88       85           True        False
2  Pooja    78       80       82          False         True

###############################################################"""

import pandas as pd


def operation():
    df=pd.read_csv("StudentMarks.csv")
    
    print("Dataset loade succesfully")
    print(df)
    
    genders = ['Male', 'Female']
    df['Gender'] = df.index.map(lambda i: 'Male' if i % 2 == 0 else 'Female')
 
    df = pd.get_dummies(df, columns=['Gender'])
    
    print(df)

def main():
    operation()
    
if __name__=="__main__":
    main()