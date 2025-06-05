def Increase(A):
    return A+1

def Demo(Taks,Value):
    for No in Value:
        print(Taks(No))
        
Data=[13,17,10,14,11]

Demo(Increase,Data)
