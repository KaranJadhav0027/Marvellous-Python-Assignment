"""############################################################
  Program Contain check Vowel and Consonant
  
Input:
Enter Character :D

Output:
D  is a Consonant

###############################################################"""

# def CheckVowel(char):

#     if char=='a'or char=='e'or char=='i'or char=='o'or char=='u':
#         return True
#     else:
#         return False

CheckVowel=lambda char:char=='a'or char=='e'or char=='i'or char=='o'or char=='u'
    
def main():
    print("Enter Character :",end="")
    Character=input()

    Ret=CheckVowel(Character)
       
    if True==Ret:
        print(Character," is a Vowel")
    else:
        print(Character," is a Consonant")

if __name__=="__main__":
    main()