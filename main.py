import streamlit as st
from calc import parse_expression, tokenize

st.title("Calculator by Tomasz Burnejko")

st.write("---")

equation_string = st.text_input(label="Wprowadź równanie: ")
st.write("Wynik to: ", parse_expression(tokenize(equation_string)))

st.write("Dziękuję za skorzystanie z kalkulatora!")
st.write("---")
