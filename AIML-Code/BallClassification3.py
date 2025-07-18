from sklearn import tree

#rough 0
#smooth 1

#tennis=1
#Cricket=2
def main():
    BallFetures=[[35,0],[47,0],[90,1],[48,0],[90,1],[35,0],[92,1],[35,0],[35,0],[35,0]]
    
    BallNames=[1,1,2,1,2,1,2,1,1,1]

    obj=tree.DecisionTreeClassifier()
   
    obj=obj.fit(BallFetures,BallNames)

    print(obj.predict([[93,1]]))

if __name__=="__main__":
    main()