"""############################################################
Output:
Dataset loade succesfully
    Name  Math  Science  English  Total
0   Amit    85       92       75    252
1  Sagar    90       88       85    263
2  Pooja    78       80       82    240
Data pass and fail:
    Name  Math  Science  English  Total status
0   Amit    85       92       75    252   Pass
1  Sagar    90       88       85    263   Pass
2  Pooja    78       80       82    240   Fail


Students Pass: 2
###############################################################"""

import pandas as pd

def operation():
    Count=0
    df=pd.read_csv("Student2.csv")
    
    print("Dataset loade succesfully")
    print(df)

    df['status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')

    print("Data pass and fail:")
    print(df)
    
    for status in df['status']:
        if status == 'Pass':
            Count += 1
    print("Students Pass:", Count)

    
def main():
    operation()
    
if __name__=="__main__":
    main()