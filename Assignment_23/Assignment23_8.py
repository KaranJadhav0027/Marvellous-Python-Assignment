
import pandas as pd
import matplotlib.pyplot as plt

def operation():
    df=pd.read_csv("Student2.csv")
    
    print("Dataset loade succesfully")
    print(df)
  
    amit = df[df["Name"] == "Amit"]

    marks = amit.drop(columns=["Name", "Total"]).squeeze()

    plt.figure(figsize=(8, 5))
    plt.plot(marks.index, marks.values, marker='o', linestyle='-', color='green')
    plt.title("Amit's Marks Across all Subjects")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.show()

def main():
    operation()
    
if __name__=="__main__":
    main()