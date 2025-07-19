"""############################################################
  program Show the Basic function used in csv
  
Output:
 Dataset loade succesfully

Shape of StudentCSV : (3, 4)

Columns in CSV : Index(['Name', 'Math', 'Science', 'English'], dtype='object')

Data type in csv : 
[['Amit' 85 92 75]
 ['Sagar' 90 88 85]
 ['Pooja' 78 80 82]]


###############################################################"""

import pandas as pd

def operation():
    df=pd.read_csv("StudentMarks.csv")
    print("Dataset loade succesfully")
    print("Shape of StudentCSV :",df.shape)
   
    print("Columns in CSV :",df.columns)

    print("Data type in csv :",df.values)  
    
def main():
    operation()
    
if __name__=="__main__":
    main()