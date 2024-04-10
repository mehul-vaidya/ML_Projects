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


loaded_model = pickle.load(open('customer_segmentation_cluster_prediction_model.pkl', 'rb'))

def customer_cluster_prediction(input_data):
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
    
    st.title('Customer Segment Cluster prediction')  

    #take input from user
    with st.form("Form 1",clear_on_submit=True):
      Annual_Income = st.text_input('Enter Annual_Income')
      spending_score = st.text_input('Enter Spending_score (1-100)')
      s_state=st.form_submit_button('Predict Cluster Number')
      if s_state:
        error=False
        if(Annual_Income.isdigit() and spending_score.isdigit() and int(spending_score)>0 and int(spending_score)<100):
          Annual_Income=int(Annual_Income)/1000
          spending_score=int(spending_score)
          
          prediction = customer_cluster_prediction([Annual_Income,spending_score])
          st.success("Customer belongs to " + str(prediction) + "th cluster")  
        else:
          st.error("Entered Data is Incorrect")  

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  