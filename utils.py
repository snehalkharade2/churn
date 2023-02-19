import pickle
import json
import config
import numpy as np

class Churn():
    def __init__(self,tenure, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, gender, SeniorCitizen, Partner, Dependents, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies):
        self.tenure = tenure
        self.Contract = Contract
        self.PaperlessBilling = PaperlessBilling
        self.PaymentMethod = PaymentMethod
        self.MonthlyCharges = MonthlyCharges
        self.TotalCharges = TotalCharges
        self.gender = gender
        self.SeniorCitizen = SeniorCitizen
        self.Partner = Partner
        self.Dependents = Dependents
        self.PhoneService = PhoneService
        self.MultipleLines = MultipleLines
        self.InternetService = InternetService
        self.OnlineSecurity = OnlineSecurity
        self.OnlineBackup = OnlineBackup
        self.DeviceProtection = DeviceProtection
        self.TechSupport = TechSupport
        self.StreamingTV = StreamingTV
        self.StreamingMovies = StreamingMovies

    def __load_model(self):

        with open(config.LASSO_MODEL_FILE_PATH,"rb") as f:
            self.log_reg = pickle.load(f)
            print("Lasso Model :: ",self.log_reg)


        with open(config.JSON_FILE_PATH,"r") as f:
            self.project_data = json.load(f)
            print("PROJECT Data :: ",self.project_data)

    def get_churn_prediction(self):
        self.__load_model()
        test_array = np.zeros((1,self.log_reg.n_features_in_))
        test_array[0][0] = self.tenure
        test_array[0][1] = self.project_data["PaperlessBilling"][self.PaperlessBilling]
        test_array[0][2] = self.MonthlyCharges
        test_array[0][3] = self.TotalCharges
        test_array[0][4] = self.project_data["Gender"][self.gender]
        test_array[0][5] = self.SeniorCitizen
        test_array[0][6] = self.project_data["Partner"][self.Partner]
        test_array[0][7] = self.project_data["Dependents"][self.Dependents] 
        test_array[0][8] = self.project_data["PhoneService"][self.PhoneService]
        test_array[0][9] = self.project_data["MultipleLines"][self.MultipleLines]
        test_array[0][10] = self.project_data["OnlineSecurity"][self.OnlineSecurity]
        test_array[0][11] = self.project_data["OnlineBackup"][self.OnlineBackup]
        test_array[0][12] = self.project_data["DeviceProtection"][self.DeviceProtection]
        test_array[0][13] = self.project_data["TechSupport"][self.TechSupport]
        test_array[0][14] = self.project_data["StreamingTV"][self.StreamingTV]
        test_array[0][15] = self.project_data["StreamingMovies"][self.StreamingMovies] 

        Contract = "Contract_" + self.Contract
        index = self.project_data["Column Names"].index(Contract)        

        PaymentMethod = "PaymentMethod_" + self.PaymentMethod
        index = self.project_data["Column Names"].index(PaymentMethod)

        InternetService = "InternetService_" + self.InternetService
        index = self.project_data["Column Names"].index(InternetService)

        test_array[0][index] = 1

        print("Test Array", test_array)

        churn_predict = self.log_reg.predict(test_array)[0]
        print("Status of the Churn ::",churn_predict)
        return churn_predict
