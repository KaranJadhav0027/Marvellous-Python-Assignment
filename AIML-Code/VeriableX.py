

#def Function_Name(*__) Kiti pan argument geyei
def Display(*A):  #nahi kahi tr pass lihayacha
    print(type(A))    # type is Tuple
    print("Inside Display",A)
   

def main():
    Display(11,21,51,101)
    Display(11,21,51,101,111) #Aranias Call
    Display(11,21,51)
    Display(11)
    Display()

if __name__ == "__main__":
    main()