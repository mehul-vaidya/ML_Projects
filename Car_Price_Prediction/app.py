"""
#conda create -p venv python==3.9
#conda activate [venv]
#pip install -r requirements.txt
#need below libraby for running jupyter notebook
#pip install ipykernel 
#streamlit run app.py
"""

import numpy as np
import pickle
import streamlit as st


loaded_model = pickle.load(open('trained_load_grant_prediction_model.pkl', 'rb'))

def loan_grant_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    return prediction[0]

    '''
    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
    '''  
  
def main():
    
    st.title('Loan Granting Prediction Web App')  

    #take input from user
    with st.form("Form 1",clear_on_submit=True):
      #Gender = st.text_input('Gender')
      Gender = st.radio("Gender",["Male", "Female"] )
      #Married = st.text_input('Married')
      Married = st.radio("Married",["Yes", "No"] )
      #Dependents = st.text_input('Dependents')
      Dependents = st.radio("No_of_Dependents",["0","1","2","3","3+"] )
      #Education = st.text_input('Education')
      Education = st.radio("Graduate",["Yes","No"])
      #Self_Employed = st.text_input('Self_Employed')
      Self_Employed = st.radio("Self_Employed",["Yes","No"])

      ApplicantIncome = st.text_input('ApplicantIncome')
      CoapplicantIncome = st.text_input('CoapplicantIncome')
      LoanAmount = st.text_input('LoanAmount')
      Loan_Amount_Term = st.text_input('Loan_Amount_Term')


      Credit_History = st.radio("Credit_History_Available",["Yes","No"])
      Property_Area = st.radio("Property_Area",["Rural","Semiurban","Urban"])

      s_state=st.form_submit_button('Loan Granting Prediction')
      if s_state:
        Gender=1 if Gender=="Male" else 0
        Married = 1 if Married=="Yes" else 0
        Dependents = 4 if Dependents=="3+" else int(Dependents)
        Education = 1 if Education=="Yes" else 0
        Self_Employed = 1 if Self_Employed=="Yes" else 0
        Credit_History = 1 if Credit_History=="Yes" else 0
        Property_Area = 0 if Property_Area=="Rural" else 1 if Property_Area=="Semiurban" else 2

        error=False
        if(ApplicantIncome.isdigit() and CoapplicantIncome.isdigit() and LoanAmount.isdigit() and Loan_Amount_Term.isdigit()):
          ApplicantIncome=float(ApplicantIncome)
          CoapplicantIncome=float(CoapplicantIncome)
          LoanAmount=float(LoanAmount)
          Loan_Amount_Term=float(Loan_Amount_Term)
          
          prediction = loan_grant_prediction([Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area  ])
          if(prediction==1):
             st.success("Loan can be granted")  
          if(prediction==0):
             st.success("Loan should not be  granted")    
                    
        else:
          st.error("You have entered non numeric data")  

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  