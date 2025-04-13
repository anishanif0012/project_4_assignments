import streamlit as st
import joblib

st.title("Streamlit Fundamentals")

st.header("This is a Header")

st.subheader("This is a Subheader")

st.text("This is a simple text output.")

st.markdown("**This is bold text using markdown**")

name = "Anis"
number = 10

st.write("Hello", name)
st.write("Here is a random number", number)

if st.button("Click me"):
    st.write("Button clicked")

checked = st.checkbox("Check me!") 

if checked:
    st.write("Checkbox is checked!")

age = st.slider("Select your age",0,100,25)
st.write("Your age is", age)

name = st.text_input("Enter your name", value= "")
st.write("Hello", name)



