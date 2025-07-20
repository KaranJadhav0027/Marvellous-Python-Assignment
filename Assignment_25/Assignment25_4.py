"""############################################################
OutPut:
DataFrame:
  Department
0         HR
1         IT
2    Finance
3         HR
4         IT

after One Hot Encoding:
   Department_Finance  Department_HR  Department_IT
0               False           True          False
1               False          False           True
2                True          False          False
3               False           True          False
4               False          False           True

###############################################################"""

import pandas as pd

def operation():
    data={'Department':['HR','IT','Finance','HR','IT']}
    df = pd.DataFrame(data)
    
    print(" DataFrame:")
    print(df)
    
    df = pd.get_dummies(df, columns=['Department'])
    
    print("after One Hot Encoding:")
    print(df)
    
  
def main():
    operation()
    
if __name__=="__main__":
    main()