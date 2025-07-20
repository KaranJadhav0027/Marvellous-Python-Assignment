"""############################################################
OutPut:
 DataFrame:
   Marks
0   85.0
1    NaN
2   90.0
3    NaN
4   95.0


   Marks
0   85.0
1   90.0
2   90.0
3   90.0
4   95.0


###############################################################"""

import pandas as pd

def operation():
   # data={'Marks':[85,No,90,np.nan,95]}
    data={'Marks':[85,None,90,None,95]}
    df = pd.DataFrame(data)
    
    print(" DataFrame:")
    print(df)
    
    df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
    print(df)

def main():
    operation()
    
if __name__=="__main__":
    main()