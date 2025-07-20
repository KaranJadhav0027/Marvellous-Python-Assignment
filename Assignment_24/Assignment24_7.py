"""############################################################
Output:
 is created 'Student24.csv'
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

    df.to_csv("Student24.csv", index=False)
    print("is created 'Student24.csv'")


    
def main():
    operation()
    
if __name__=="__main__":
    main()