"""############################################################
    A program that print first 10 even Number

OutPut:
2  4  6  8  10  12  14  16  18  20

###############################################################"""

def Display():
   
    for i in range(2,21,2):
        print(i,end="  ")
    
def main():

    Display()

if __name__ == "__main__":
    main()