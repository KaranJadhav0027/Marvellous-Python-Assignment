"""############################################################
OutPut:
  Name   Age
0    A  21.0
1    B  22.0
2    C  23.0

  Name  Age
0    A   21
1    B   22
2    C   23

###############################################################"""

import pandas as pd

def operation():
    data={'Name':['A','B','C'],'Age':[21.0,22.0,23.0]}
    df = pd.DataFrame(data)
    print(df)

    df['Age'] = df['Age'].astype(int)

    print(df)
  
def main():
    operation()
    
if __name__=="__main__":
    main()