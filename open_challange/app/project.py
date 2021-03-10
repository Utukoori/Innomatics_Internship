import streamlit as st

import data_app as da
# required libraries
import numpy as np
import pandas as pd
##import seaborn as sns
#import matplotlib.pyplot as plt

from pickle import load,dump
#from sklearn.svm import SVC

def x_values():
    x1 = st.number_input("Enter col1 value: ")
    x2 = st.number_input("Enter col2 value: ")
    x = x1,x2
    x = np.array(x)
    return x.reshape(1,-1)
@st.cache
def predict(x):
    #loading svc rbf model
    #from sklearn.svm import SVC
    model = load(open('pickle/svc_rbf_model.pkl', 'rb'))
    result = model.predict(x)
    return result

def main():
    st.title('Support Vector Classifier')
    da.main()
    st.header("Prediction")
    x = x_values()# loading x values
    result = predict(x)

    if st.button('Submit'):
        if result == 0:
            st.write('No result is 0  :cry:')
        else:
            st.write('Yes result is 1:sunglasses:')

if(__name__ == '__main__'):
    main()
