
# coding: utf-8
from flask import Flask, request, render_template  # type: ignore
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/", methods=['GET'])
def loadPage():
	return render_template('index.html')


@app.route("/", methods=['POST'])
def predict():
    if request.method == 'POST':        
        SeniorCitizen = request.form['Senior Citizen']
        if(SeniorCitizen == 'Yes'):
            SeniorCitizen = 1
        else:
            SeniorCitizen = 0

        tenure = int(request.form['Tenure'])
        MonthlyCharges= float(request.form['Monthly Charges'])
        TotalCharges= float(request.form['Total Charges'])

       
        Gender= request.form['Gender']       
        if(Gender == 'Male'):
            gender_Male = 1
            gender_Female = 0
        else:
            gender_Male = 0
            gender_Female = 1


        
        Partner= request.form['Partner']
        if(Partner == 'Yes'):
            Partner_Yes = 1
            Partner_No = 0
        else:
            Partner_Yes = 0
            Partner_No = 1

      
        Dependents= request.form['Dependents']
        if(Dependents == 'Yes'):
            Dependents_Yes = 1
            Dependents_No = 0
        else:
            Dependents_Yes = 0
            Dependents_No = 1

        
        PhoneService= request.form['Phone Service']
        if(PhoneService == 'Yes'):
            PhoneService_Yes = 1
            PhoneService_No = 0
        else:
            PhoneService_Yes = 0
            PhoneService_No = 1

        MultipleLines= request.form['Multiple Lines']  
        if(MultipleLines == 'No phone service'):
            MultipleLines_Nophoneservice = 1
            MultipleLines_Yes = 0
            MultipleLines_No = 0
        elif(MultipleLines == 'Yes'):
            MultipleLines_Nophoneservice = 0
            MultipleLines_Yes = 1
            MultipleLines_No = 0
        else:
            MultipleLines_Nophoneservice = 0
            MultipleLines_Yes = 0
            MultipleLines_No = 1


        
        InternetService= request.form['Internet Service']
        if(InternetService == 'Fiber optic'):
            InternetService_Fiberoptic = 1
            InternetService_No = 0
            InternetService_DSL = 0
        elif(InternetService == 'No'):
            InternetService_Fiberoptic = 0
            InternetService_No = 1
            InternetService_DSL = 0
        else:
            InternetService_Fiberoptic = 0
            InternetService_No = 0
            InternetService_DSL = 1


        OnlineSecurity= request.form['Online Security']
        if(OnlineSecurity == 'No internet service'):
            OnlineSecurity_Nointernetservice = 1
            OnlineSecurity_Yes = 0
            OnlineSecurity_No = 0
        elif(OnlineSecurity == 'Yes'):
            OnlineSecurity_Nointernetservice = 0
            OnlineSecurity_Yes = 1
            OnlineSecurity_No = 0
        else:
            OnlineSecurity_Nointernetservice = 0
            OnlineSecurity_Yes = 0
            OnlineSecurity_No = 1

    
        
        OnlineBackup= request.form['Online Backup']
        if(OnlineBackup == 'No internet service'):
            OnlineBackup_Nointernetservice = 1
            OnlineBackup_Yes = 0
            OnlineBackup_No = 0
        elif(OnlineBackup == 'Yes'):
            OnlineBackup_Nointernetservice = 0
            OnlineBackup_Yes = 1
            OnlineBackup_No = 0
        else:
            OnlineBackup_Nointernetservice = 0
            OnlineBackup_Yes = 0
            OnlineBackup_No = 1
    
        DeviceProtection= request.form['Device Protection']
        if(DeviceProtection == 'No internet service'):
            DeviceProtection_Nointernetservice = 1
            DeviceProtection_Yes = 0
            DeviceProtection_No = 0
        elif(DeviceProtection == 'Yes'):
            DeviceProtection_Nointernetservice = 0
            DeviceProtection_Yes = 1
            DeviceProtection_No = 0
        else:
            DeviceProtection_Nointernetservice = 0
            DeviceProtection_Yes = 0
            DeviceProtection_No = 1
        
        TechSupport= request.form['Tech Support']
        if(TechSupport == 'No internet service'):
            TechSupport_Nointernetservice = 1
            TechSupport_Yes = 0
            TechSupport_No = 0
        elif(TechSupport == 'Yes'):
            TechSupport_Nointernetservice = 0
            TechSupport_Yes = 1
            TechSupport_No = 0
        else:
            TechSupport_Nointernetservice = 0
            TechSupport_Yes = 0
            TechSupport_No = 1 
    
        StreamingTV= request.form['Streaming TV']
        if(StreamingTV == 'No internet service'):
            StreamingTV_Nointernetservice = 1
            StreamingTV_Yes = 0
            StreamingTV_No = 0
        elif(StreamingTV == 'Yes'):
            StreamingTV_Nointernetservice = 0
            StreamingTV_Yes = 1
            StreamingTV_No = 0
        else:
            StreamingTV_Nointernetservice = 0
            StreamingTV_Yes = 0
            StreamingTV_No = 1  
        
        StreamingMovies= request.form['Streaming Movies']
        if(StreamingMovies == 'No internet service'):
            StreamingMovies_Nointernetservice = 1
            StreamingMovies_Yes = 0
            StreamingMovies_No = 0
        elif(StreamingMovies == 'Yes'):
            StreamingMovies_Nointernetservice = 0
            StreamingMovies_Yes = 1
            StreamingMovies_No = 0
        else:
            StreamingMovies_Nointernetservice = 0
            StreamingMovies_Yes = 0
            StreamingMovies_No = 1 
        
        Contract= request.form['Contract']
        if(Contract == 'One year'):
            Contract_Oneyear = 1
            Contract_Twoyear = 0
            Contract_Monthtomonth = 0
        elif(Contract == 'Two year'):
            Contract_Oneyear = 0
            Contract_Twoyear = 1
            Contract_Monthtomonth = 0
        else:
            Contract_Oneyear = 0
            Contract_Twoyear = 0
            Contract_Monthtomonth = 1  
        

        PaperlessBilling= request.form['Paperless Billing']        
        if(PaperlessBilling == 'Yes'):
            PaperlessBilling_Yes = 1
            PaperlessBilling_No = 0
        else:
            PaperlessBilling_Yes = 0
            PaperlessBilling_No = 1


        PaymentMethod= request.form['Payment Method']        
        if(PaymentMethod == 'Credit card automatic'):
            PaymentMethod_Creditcardautomatic = 1
            PaymentMethod_Electroniccheck = 0
            PaymentMethod_Mailedcheck = 0
            PaymentMethod_Banktransferautomatic = 0
        elif(PaymentMethod == 'Electronic check'):
            PaymentMethod_Creditcardautomatic = 0
            PaymentMethod_Electroniccheck = 1
            PaymentMethod_Mailedcheck = 0
            PaymentMethod_Banktransferautomatic = 0
        elif(PaymentMethod == 'Mailed check'):
            PaymentMethod_Creditcardautomatic = 0
            PaymentMethod_Electroniccheck = 0
            PaymentMethod_Mailedcheck = 1
            PaymentMethod_Banktransferautomatic = 0
        elif(PaymentMethod == 'Bank transfer automatic'):
            PaymentMethod_Creditcardautomatic = 0
            PaymentMethod_Electroniccheck = 0
            PaymentMethod_Mailedcheck = 0
            PaymentMethod_Banktransferautomatic = 1
        else:
            PaymentMethod_Creditcardautomatic = 0
            PaymentMethod_Electroniccheck = 0
            PaymentMethod_Mailedcheck = 0
            PaymentMethod_Banktransferautomatic = 0
        
        input_data = ([[SeniorCitizen, tenure, MonthlyCharges, TotalCharges, gender_Male, Partner_Yes, Dependents_Yes, PhoneService_Yes, MultipleLines_Nophoneservice, MultipleLines_Yes, InternetService_Fiberoptic, InternetService_No, OnlineSecurity_Nointernetservice, OnlineSecurity_Yes, OnlineBackup_Nointernetservice, OnlineBackup_Yes, DeviceProtection_Nointernetservice, DeviceProtection_Yes, TechSupport_Nointernetservice, TechSupport_Yes,StreamingTV_Nointernetservice, StreamingTV_Yes, StreamingMovies_Nointernetservice, StreamingMovies_Yes, Contract_Oneyear, Contract_Twoyear, PaperlessBilling_Yes, PaymentMethod_Creditcardautomatic, PaymentMethod_Electroniccheck, PaymentMethod_Mailedcheck]])   
        pred = model.predict(input_data)
        prob = model.predict_proba(input_data)[0]
        
        pred_class_index = np.argmax(prob)                
        prob = prob[pred_class_index]
        
        probability = "Accuracy: {:.2f} %".format(prob * 100)
        
        if pred == 1:
            prediction_text = "We're sorry to see you go!"
            text_color = "red" 
            emoji = "😔" 
        else:
            prediction_text = "Congratulations!! We hope you're enjoying our services."
            text_color = "blue" 
            emoji = "😊" 
        return render_template('index.html', prediction_text=prediction_text, emoji=emoji, pred_prob=probability, text_color=text_color)      
        
if __name__=="__main__":        
    app.run(debug=True)









