"""############################################################
OutPut:
 DataFrame:
   Marks
0     45
1     67
2     88
3     32
4     76

  Marks
0  Fail
1    67
2    88
3  Fail
4    76

###############################################################"""

import pandas as pd


def operation():
    data={'Marks':[45,67,88,32,76]}
    df = pd.DataFrame(data)
    
    print(" DataFrame:")
    print(df)
   
    df['Marks'] = df['Marks'].where(df['Marks'] >= 50, 'Fail')
    print(df)
def main():
    operation()
    
if __name__=="__main__":
    main()