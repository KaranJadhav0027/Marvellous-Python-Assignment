"""############################################################
  Program Contain check Vowel and Consonant
  
Input:
Enter Your Age  :45

Output:
45  Eligible to Vote

Input:
Enter Your Age  :-75

Output:
Enter Age Greater than Zero(0)
-75 Not Eligible to Vote

###############################################################"""

# def CheckAge(Value):
#     if Value<0:
#         print("Enter Age Greater than Zero(0) ")
#         return
#     elif Value>18 :
#         return True
#     else:
#         return False

CheckAge=lambda Value:Value>18
    
def main():
    print("Enter Your Age  :",end="")
    Age=int(input())

    Ret=CheckAge(Age)
       
    if True==Ret:
        print(Age," Eligible to Vote")
    else:
        print(Age,"Not Eligible to Vote")

if __name__=="__main__":
    main()