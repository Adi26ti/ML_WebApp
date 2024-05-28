# -*- coding: utf-8 -*-
"""
Created on Mon May 27 12:11:28 2024

@author: Aditi
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

a=pickle.load(open('Diabetes_model.sav','rb'))
b=pickle.load(open('Parkinsons_model.sav','rb'))
c=pickle.load(open('Heart_model.sav','rb'))

with st.sidebar:
    om=option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Heart Diasease Prediction','Parkinsons Prediction'], icons=['activity','heart','person'], default_index=0)
    #=0 means defaut open page will be diaetes =1 will be heart
    
if(om=='Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    c1,c2,c3=st.columns(3)
    with c1:
        Pregnancies=st.text_input('No. of Pregnancies')
    with c2:
        Glucose=st.text_input('Glucose Level') 
    with c3:
        BloodPressure=st.text_input('Blood Pressure Level') 
    with c1:
        SkinThickness=st.text_input('Skinv Thickness value') 
    with c2:
        Insulin=st.text_input('Insulin  Level')
    with c3:
        BMI=st.text_input('BMI value')
    with c1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value') 
    with c2:
        Age=st.text_input('Age of patient') 
    diagnosis=''
    if st.button('Diabetes Test Result'):
        diagnosis=a.predict([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
        if(diagnosis[0]==0):
          diagnosis='The patient is not Diabetic'
        else:
          diagnosis='The patient is Diabetic'
  
    st.success(diagnosis)
    
if(om=='Heart Diasease Prediction'):
    st.title('Heart Diasease Prediction using ML')
    c1,c2,c3=st.columns(3)
    with c1:
        age=st.text_input('age')
    with c2:
        sex=st.text_input('sex')
    with c3:
        cp=st.text_input('cp')
    with c1:
        trestbps=st.text_input('trestbps')
    with c2:
        chol=st.text_input('chol') 
    with c3:
        fbs=st.text_input('fbs') 
    with c1:
        restecg=st.text_input('restecg') 
    with c2:
        thalach=st.text_input('thalach') 
    with c3:
        exang=st.text_input('exang') 
    with c1:
        oldpeak=st.text_input('oldpeak')
    with c2:
        slope=st.text_input('slope') 
    with c3:
        ca=st.text_input('ca')
    with c1:
        thal=st.text_input('thal')    
    result=''
    if st.button('Heart Disease Result'):
        result=c.predict([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
    
        if(result[0]==1):
          result='Patient has Heart Disease'
        else:
          result='Patient do not have Heart Disease'
    st.success(result)
    
if(om=='Parkinsons Prediction'):
    st.title('Parkinsons Prediction using ML')
    c1,c2,c3=st.columns(3)
    with c1:
        MDVPFo=st.text_input('MDVP:Fo(Hz)')
    with c2:
        MDVPFhi=st.text_input('MDVP:Fhi(Hz)')
    with c3:
        MDVPFlo=st.text_input('MDVP:Flo(Hz)')
    with c1:
        MDVPJitterp=st.text_input('MDVP:Jitter(%)') 
    with c2:
        MDVPJitterAbs=st.text_input('MDVP:Jitter(Abs)')
    with c3:
        MDVPRAP=st.text_input('MDVP:RAP')
    with c1:
        MDVPPPQ=st.text_input('MDVP:PPQ')
    with c2:
        JitterDDP=st.text_input('Jitter:DDP')
    with c3:
        MDVPShimmer=st.text_input('MDVP:Shimmer')
    with c1:
        MDVPShimmerdb=st.text_input('MDVP:Shimmer(dB)') 
    with c2:
        ShimmerAPQ3=st.text_input('Shimmer:APQ3') 
    with c3:
        ShimmerAPQ5=st.text_input('Shimmer:APQ5')
    with c1:
        MDVPAPQ=st.text_input('MDVP:APQ')
    with c2:
        ShimmerDDA=st.text_input('Shimmer:DDA')
    with c3:
        NHR=st.text_input('NHR') 
    with c1:
        HNR=st.text_input('HNR') 
    with c2:
        RPDE=st.text_input('RPDE')
    with c3:
        DFA=st.text_input('DFA') 
    with c1:
        spread1=st.text_input('spread1')
    with c2:
        spreada=st.text_input('spread2') 
    with c3:
        D2a=st.text_input('D2')
    with c1:
        PPE=st.text_input('PPE')
    result=''
    if st.button('Parkinsons Result'):
        result=b.predict([MDVPFo,MDVPFhi,MDVPFlo,MDVPJitterp,MDVPJitterAbs,MDVPRAP,MDVPPPQ,JitterDDP,MDVPShimmer,MDVPShimmerdb,ShimmerAPQ3,ShimmerAPQ5,MDVPAPQ,ShimmerDDA,NHR,HNR,RPDE,DFA,spread1,spreada,D2a,PPE])
        
        if(result[0]==1):
          result='Patient has Parkinsons Disease'
        else:
          result='Patient do not have Parkinsons Disease'
    st.success(result)

