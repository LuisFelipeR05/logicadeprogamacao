import streamlit as st

st.title("Calculadora De IMC!")


peso = st.number_input("Digite seu peso:",step=1)
altura = st.number_input("Digite sua altura:",min_value=0.1)

IMC = peso / altura**2


st.text(f" O Seu IMC é igual {IMC:.2f}")