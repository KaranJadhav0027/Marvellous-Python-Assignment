"""############################################################

  Bar Plot Student VS Total 
###############################################################"""

import pandas as pd
import matplotlib.pyplot as plt

def operation():
    df=pd.read_csv("Student2.csv")
    
    print("Dataset loade succesfully")
    print(df)
  
    plt.figure(figsize=(10, 6))
    plt.bar(df["Name"], df["Total"], color='skyblue')
    plt.title("Student Name vs Total Marks")
    plt.xlabel("Student Name")
    plt.ylabel("Total Marks")
    plt.show()

def main():
    operation()
    
if __name__=="__main__":
    main()