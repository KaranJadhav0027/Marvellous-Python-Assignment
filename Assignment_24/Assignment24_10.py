
import pandas as pd
import matplotlib.pyplot as plt

def operation():
    df=pd.read_csv("Student2.csv")
    
    print("Dataset loade succesfully")
    print(df)

      
    plt.figure(figsize=(6, 4))
    plt.boxplot(df['English'].dropna())  
    plt.title('Boxplot of English Marks')
    plt.ylabel('Marks')
    plt.grid(True)
    plt.show()
    
def main():
    operation()
    
if __name__=="__main__":
    main()