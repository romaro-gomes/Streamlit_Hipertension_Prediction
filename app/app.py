import streamlit as st
import pandas as pd
import pickle

from PIL import Image
image_good=Image.open('./good.jpg')
image_worse=Image.open('./bad.jpg')

st.title('Hipertension Predict Model')
st.markdown("The model's aim is to assist doctors in making decisions about patient health by utilizing clinical history and lifestyle data")
def gender_label(label):
    if label=='M':
        return 1
    else:
        return 0

def chest_pain_label(label):
    if label=='Asymptomatic':
        return 0
    elif label=='Typical Angina':
        return 1
    elif label=='Atypical Angine':
        return 2
    elif label=='Non-Annginal Pain':
        return 3

def true_false_label(label):
    if label=='Yes':
        return 1
    else:
        return 0

def slope_label(label):
    if label=='Upsloping':
        return 0
    elif label=='Flat':
        return 1
    elif label=='Downsloping':
        return 2
    
def thal_label(label):
    if label=='Normal':
        return 0
    elif label=='Fixed Defect':
        return 1
    elif label=='Reversable Defect':
        return 2

def restcg_label(label):
    if label=='Normal':
        return 0
    elif label=='ST-T wave abnormality':
        return 1
    elif label=='Probable or Definite Left Ventricular Hypertrophy':
        return 2

def hypertension_prediction():
    st.header('Complete the Patient Clinical Information.',divider='blue')

    sex=st.selectbox('Sex',('M','F'))                
    age=st.slider('Age',10.0,90.0,110.0)                           
    fbs=st.selectbox("The patient's fasting blood sugar > 120 mg/dl",('No','Yes'))        
    ca=st.selectbox('Number of major vessels colored by flourosopy',(0,1,2,3,4))         
    cp=st.selectbox('Chest pain type',('Asymptomatic', 'Typical Angina', 'Atypical Angine', 'Non-Annginal Pain'))            
    restecg=st.selectbox('Resting ECG results',('Normal','ST-T wave abnormality','Probable or Definite Left Ventricular Hypertrophy'))       
    trestbps=st.slider('Resting blood pressure (in mmHg)',90.0,210.0,100.0)    
    thalach=st.slider('Maximum heart rate achieved',70.0,210.0,100.0)                   
    exang=st.selectbox('Exercise Induced Angina',('No','Yes'))    
    oldpeak=st.slider('ST Depression Induced by Exercise Relative to Rest',0.0,7.0,1.0)
    slope=st.selectbox('The Slope of The Peak Exercise ST Segment',('Upsloping','Flat','Downsloping'))  
    thal=st.selectbox('Thallium-201 Result',('Normal','Fixed Defect','Reversable Defect'))
    chol=st.slider('Serum cholestoral in mg/dl',125.0,570.0,250.0) 


    data= {                            
        'age':age,
        'sex':gender_label(sex),
        'cp':chest_pain_label(cp),
        'trestbps':trestbps,
        'chol':chol,                                     
        'fbs':true_false_label(fbs),
        'restecg':restcg_label(restecg),
        'thalach':thalach,
        'exang':true_false_label(exang),
        'oldpeak':oldpeak,
        'slope':slope_label(slope),                  
        'ca':ca,           
        'thal':thal_label(thal) 
    }
            
                    
    features = pd.DataFrame(data,index=[0])
    return features

df=hypertension_prediction()

if st.button('Predict'):
    model=pickle.load(open('hypertension_model.pkl','rb'))
    predict=model.predict(df)   

    if predict == 0:
         
         st.image(image_good, caption='Health Blood System')
         st.markdown("""
         The pataient's  lifestyle and clinical history indicate a healthylife. 
         """)
    else:

         st.image(image_worse, caption='You need help')
         st.markdown("""
         The patient's lifestyle and clinical history indicate the need for medical assistance.
         """)
