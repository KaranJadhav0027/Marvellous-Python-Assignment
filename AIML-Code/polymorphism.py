#method overloading not Allowed
class Demo:
    def Addition(A,B):
        return A+B
    
    def Addition(A,B,C):
        return A+B+C
    
obj=Demo()

print(obj.Addition(10,11))
print(obj.Addition(10,11,21))
