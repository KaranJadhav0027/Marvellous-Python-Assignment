from sklearn.metrics import r2_score

def main():
   y_actual=[100,200,300,400,500]

   y_pred=[150,150,350,350,550]

   r2=r2_score(y_actual,y_pred)

   print("Actual Values :",y_actual)
   print("Predicted Value :",y_pred)

   print("R2 Value ",r2)
    
if __name__=="__main__":
    main()