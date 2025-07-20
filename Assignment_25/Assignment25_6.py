"""############################################################
OutPut:
 DataFrame:
  Gread
0    A+
1     B
2     A
3     C
4    B+

       Gread
0  Excellent
1    Average
2  Very Good
3       Poor
4       Good

###############################################################"""

import pandas as pd


def operation():
    data={'Gread':['A+','B','A','C','B+']}
    df = pd.DataFrame(data)
    
    print(" DataFrame:")
    print(df)
   
    grade_map = {
        'A+': 'Excellent',
        'A': 'Very Good',
        'B+': 'Good',
        'B': 'Average',
        'C': 'Poor'
    }
    
    df['Gread'] = df['Gread'].map(grade_map)
    print(df)
  
def main():
    operation()
    
if __name__=="__main__":
    main()