from sklearn import tree

def main():
    BallFetures=[[35,"rough"],[47,"rough"],[90,"smooth"],[48,"rough"],[90,"smooth"],[35,"rough"],[92,"smooth"],[35,"rough"],[35,"rough"],[35,"rough"]]
    
    BallNames=["tennis","tennis","cricket","tennis","cricket","tennis","cricket","tennis","tennis","tennis"]

    obj=tree.DecisionTreeClassifier()
   
    obj=obj.fit(BallFetures,BallNames)

    print(obj.predict([93,"smooth"]))

if __name__=="__main__":
    main()