import numpy as np
from sklearn.metrics import mean_squared_error,r2_score

def main():
    y_actual=[10,20,30,40,50]
    y_predicted=[14,16,34,36,54]

    MSE=mean_squared_error(y_actual,y_predicted)

    RMSE=np.sqrt(MSE)

    print("Actual Value :",y_actual)
    print("Predicted Value :",y_predicted)
    print("Mean Square Error :",MSE)
    print("Root Mean Square Error :",RMSE)
    
if __name__=="__main__":
    main()