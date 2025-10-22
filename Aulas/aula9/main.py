import streamlit as st

st.title("Ola, Mundo!")

dolar = st.number_input("dolar" ,placeholder = "Digite o Valor em Dolar:")

reais = dolar * 5.40

st.text(f"O Valor de {dolar} dolares é igual a {reais:.2f} Reais. ")