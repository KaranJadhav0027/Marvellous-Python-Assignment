"""############################################################
  program Show the  Descriptive Statistics function used in csv
  
Output:
Dataset loade succesfully
Shape of StudentCSV : (3, 4)
Used Descriptive Statistics :
            Math    Science    English
count   3.000000   3.000000   3.000000
mean   84.333333  86.666667  80.666667
std     6.027714   6.110101   5.131601
min    78.000000  80.000000  75.000000
25%    81.500000  84.000000  78.500000
50%    85.000000  88.000000  82.000000
75%    87.500000  90.000000  83.500000
max    90.000000  92.000000  85.000000

###############################################################"""

import pandas as pd

def operation():
    df=pd.read_csv("StudentMarks.csv")

    print("Dataset loade succesfully")

    print("Shape of StudentCSV :",df.shape)
   
    print("Used Descriptive Statistics :")
    print(df.describe())

    
def main():
    operation()
    
if __name__=="__main__":
    main()