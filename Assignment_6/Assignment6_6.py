"""############################################################
   program contain Pattern print
 
Output:
        *
        *       *
        *       *       *
        *       *       *       * 
###############################################################"""

def Pattern():
 
    for i in range(1,5):
       for j in range(0,i):
           print("\t*",end="")
       print(" ")
                  
def main():

    Pattern() 
    
if __name__=="__main__":
    main()