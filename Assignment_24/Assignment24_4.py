"""############################################################


###############################################################"""

import pandas as pd
import matplotlib.pyplot as plt

def operation():
    df=pd.read_csv("StudentMarks.csv")
    
    print("Dataset loade succesfully")
    print(df)
    
    data = df[df['Name'] == 'Sagar']

    marks = data.drop(columns=['Name']).iloc[0]
 
    plt.figure(figsize=(8, 6))
    plt.pie(marks, labels=marks.index, autopct='%1.1f%%', startangle=140)
    plt.title("Subject marks for Sagar")
    plt.axis('equal')  
    plt.show()

    
def main():
    operation()
    
if __name__=="__main__":
    main()