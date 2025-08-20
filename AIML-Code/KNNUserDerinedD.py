#     A,B,C,D
# X : 1,2,3,6
# Y : 2,3,1,5
#     R,R,B,B
import numpy as np
import math

def EucDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)
    return Ans

def MarvellousKNN():
    line = "-"*80
    data = [{'point': 'A', 'X' : 1, 'Y' : 2, 'label' : 'Red'},
            {'point': 'B', 'X' : 2, 'Y' : 3, 'label' : 'Red'},
            {'point': 'C', 'X' : 3, 'Y' : 1, 'label' : 'Blue'},
            {'point': 'D', 'X' : 6, 'Y' : 5, 'label' : 'Blue'}]
    
    print(line)
    print("Training Data set : ")
    print(line)
    
    for i in data:
        print(i)
    print(line)
    
    new_point = {'X' : 3, 'Y' : 3}
    
    # Calculate the distances
    for d in data:
        d['distance'] = EucDistance(d, new_point)
        
    print(line)
    print("Calculated Distances are : ")
    print(line)
    
    for d in data:
        print(d)
        
    print(line)
    
    # Sort by distance
    sorted_data = sorted(data, key = lambda item : item['distance'])
    
    print(line)
    print("Sorted data is : ")
    print(line)
    
    for d in sorted_data:
        print(d)  
    print(line)
    
    K = 3
    nearest = sorted_data[:K]
    
    print(line)
    print("Sorted 3 elements are : ")
    print(line)
    
    for d in nearest:
        print(d)
    print(line)
    
    # Voting
    votes ={}
    for neighbour in nearest:
        label = neighbour['label']
        votes['label']=votes.get(label,0)+1
    
    print(line)
    print("Result of voting is :")

    for d in votes:
        print("Name :",d,"value:",votes[d])
    
    print(line)
    
def main():
    print("Demonstartion of KNN algorithm")
    MarvellousKNN()
    
if __name__ == "_main_":
    main()