import streamlit as st

st.title("Calculator by Tomasz Burnejko")

st.write("---")

equation_string = st.text_input(label="Wprowadź równanie: ")
st.write("Wynik to: ", equation_string)

st.write("Dziękuję za skorzystanie z kalkulatora!")
st.write("---")
