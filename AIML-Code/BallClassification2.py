from sklearn import tree

#rough 0
#smooth 1
def main():
    BallFetures=[[35,0],[47,0],[90,1],[48,0],[90,1],[35,0],[92,1],[35,0],[35,0],[35,0]]
    
    BallNames=["tennis","tennis","cricket","tennis","cricket","tennis","cricket","tennis","tennis","tennis"]

    obj=tree.DecisionTreeClassifier()
   
    obj=obj.fit(BallFetures,BallNames)

    print(obj.predict([93,1]))

if __name__=="__main__":
    main()