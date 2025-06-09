
def checkEven(No):
    if (No%2==0):
        return True
    else:
        return False

ret=checkEven(11)
if ret==True:
    print("Number is Even")
else:
    print("Number is Odd")