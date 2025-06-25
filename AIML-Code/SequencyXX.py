
PI=3.14
def CricleArea(Rad):
      Area=Rad*Rad*PI
      return Area

def main():
    print("Enter Radius of Cricle :")
    radius=float(input())

    AreaOfCricle=CricleArea(Rad=radius)

    print("Area of Cricle is :",AreaOfCricle)


if __name__ == "__main__":
    main()