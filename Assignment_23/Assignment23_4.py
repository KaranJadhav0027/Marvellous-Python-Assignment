"""############################################################

  
Output:
Dataset loade succesfully
    Name  Math  Science  English
0   Amit    85       92       75
1  Sagar    90       88       85

###############################################################"""

import pandas as pd

def operation():
    df=pd.read_csv("StudentMarks.csv")
    
    print("Dataset loade succesfully")
    
    print(df[df['Science'] > 85])
     
def main():
    operation()
    
if __name__=="__main__":
    main()