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


loaded_model = pickle.load(open('trained_car_price_prediction_model.pkl', 'rb'))

def car_price_prediction(input_data):
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
    
    st.title('Car Price Prediction Web App')  

    #take input from user
    with st.form("Form 1",clear_on_submit=True):
      car_year = st.text_input('year')
      present_price = st.text_input('present_price in lakh')
      KM_Driven = st.text_input('KM_Driven')
      Fuel_type = st.radio("Fuel_type",["Petrol", "Diesel , CNG"] )
      seller_type = st.radio("seller_type",["Dealer", "Individual"] )
      Transmission = st.radio("Transmission",["Manual", "Automatic"] )
      Owner = st.text_input('Owner')

      s_state=st.form_submit_button('Predict Car Price')
      if s_state:
        Fuel_type = 0 if Fuel_type=="Petrol" else 1 if Fuel_type=="Diesel" else 2
        seller_type = 0 if seller_type=="Dealer" else 1
        Transmission = 0 if Transmission=="Manual" else 1

        error=False
        if(car_year.isdigit() and present_price.isdigit() and KM_Driven.isdigit() and Owner.isdigit() and int(car_year)>1900 and int(car_year)<2100 ):
          car_year=int(car_year)
          present_price=float(present_price)/100000
          KM_Driven=int(KM_Driven)
          Owner=int(Owner)

          prediction = car_price_prediction([car_year,present_price,KM_Driven,Fuel_type,seller_type,Transmission,Owner])
          st.success("Car's predicted price is " + str('{0:.2f}'.format(prediction)) + " Lakhs")  
                    
        else:
          st.error("You have entered incorrect data")  

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  