
def CricleArea(Rad,PI=3.14):
      Area=Rad*Rad*PI
      return Area

def main():
    print("Enter Radius of Cricle :")
    radius=float(input())

    AreaOfCricle=CricleArea(radius)
    #  AreaOfCricle=CricleArea(radius,7.24)

    print("Area of Cricle is :",AreaOfCricle)


if __name__ == "__main__":
    main()