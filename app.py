import streamlit as st
import pandas as pd
import xlsxwriter
import joblib 
def main():
    st.title("Iris prediction")
    model = joblib.load('iris.pkl')
    sl = st.number_input("inserisci il valore per sepal lenght",1,10,3)
    sw = st.number_input("inserisci il valore per sepal width",1,10,3)
    pl = st.number_input("inserisci il valore per petal lenght",1,10,3)
    pw = st.number_input("inserisci il valore per petal width",1,10,3)
    res = model.predict([[3,3,3,3]])[0]
    if st.button('predict'):
        st.write(res)



if __name__ == "__main__":
    main()