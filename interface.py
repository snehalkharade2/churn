from flask import Flask,render_template,request,jsonify
import config
from utils import Churn
import traceback
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/churn_status", methods = ["GET","POST"])
def churn_status():
    try:
        if request.method == "POST":
            data = request.form.get
            print("User Data is ",data)

            tenure = eval(data("tenure"))
            Contract = data("Contract")
            PaperlessBilling = data('PaperlessBilling')
            PaymentMethod = data("PaymentMethod")
            MonthlyCharges = eval(data('MonthlyCharges'))
            TotalCharges = eval(data('TotalCharges'))
            gender = data('gender')
            SeniorCitizen = eval(data('SeniorCitizen'))
            Partner = data('Partner')
            Dependents = data('Dependents')
            PhoneService = data('PhoneService')
            MultipleLines = data('MultipleLines')
            InternetService = data("InternetService")
            OnlineSecurity = data('OnlineSecurity')
            OnlineBackup = data('OnlineBackup')
            DeviceProtection = data('DeviceProtection')
            TechSupport = data('TechSupport')
            StreamingTV = data('StreamingTV')
            StreamingMovies = data('StreamingMovies')

            churn_pred = Churn(tenure, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, gender, SeniorCitizen, Partner, Dependents, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies)
            predict_churn = churn_pred.get_churn_prediction()

            if predict_churn == 0:
                return render_template("index.html",prediction = "given")
            else:
                return render_template("index.html",prediction = "Not given")

        else:
            data  = request.args.get
            print("User data is :",data)

            tenure = eval(data("tenure"))
            Contract = data("Contract")
            PaperlessBilling = data('PaperlessBilling')
            PaymentMethod = data("PaymentMethod")
            MonthlyCharges = eval(data('MonthlyCharges'))
            TotalCharges = eval(data('TotalCharges'))
            gender = data('gender')
            SeniorCitizen = eval(data('SeniorCitizen'))
            Partner = data('Partner')
            Dependents = data('Dependents')
            PhoneService = data('PhoneService')
            MultipleLines = data('MultipleLines')
            InternetService = data("InternetService")
            OnlineSecurity = data('OnlineSecurity')
            OnlineBackup = data('OnlineBackup')
            DeviceProtection = data('DeviceProtection')
            TechSupport = data('TechSupport')
            StreamingTV = data('StreamingTV')
            StreamingMovies = data('StreamingMovies')


            churn_pred = Churn(tenure, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, gender, SeniorCitizen, Partner, Dependents, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies)
            predict_churn = churn_pred.get_churn_prediction()

            if predict_churn == 0:
                return render_template("index.html",prediction = "given")
            else:
                return render_template("index.html",prediction = "Not given")

    except:
        print(traceback.print_exc())
        return jsonify({"Message" : "Unsuccessful"})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port  = config.PORT_NUMBER, debug = True)        