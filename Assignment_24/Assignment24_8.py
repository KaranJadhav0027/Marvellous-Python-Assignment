"""############################################################
Output:
 is created 'Student24.csv'
###############################################################"""

import pandas as pd
import matplotlib.pyplot as plt

def operation():
    Count=0
    df=pd.read_csv("Student2.csv")
    
    print("Dataset loade succesfully")
    print(df)

    # df['status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')

    # print("Data pass and fail:")
    # print(df)
    
    # for status in df['status']:
    #     if status == 'Pass':
    #         Count += 1
    # print("Students Pass:", Count)

    # df.to_csv("Student24.csv", index=False)
    # print("is created 'Student24.csv'")

    plt.figure(figsize=(8,5))
    plt.hist(df['Math'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Histogram of Math Marks')
    plt.xlabel('Math Marks')
    plt.ylabel('Number of Students')
    plt.grid(axis='y', alpha=0.75)
    plt.show()
    
def main():
    operation()
    
if __name__=="__main__":
    main()