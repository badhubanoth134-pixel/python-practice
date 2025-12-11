import streamlit as st
st.title("welcome to streamlit")
num1=st.number_input("Enter number 1",step=1)
num2=st.number_input("Enter number 2",step=1)
sum=num1+num2
if st.button("Add")
    st.write("sum is: ",sum)