import streamlit as st
from random import choice
from string import ascii_letters

tamanho = st.select_slider(
    "Digite o Tamanho Da senha",
    [
        5,
        6,
        7,
        8
    ]
)
aleatorio = ""

for i in range(tamanho):
    aleatorio += choice(ascii_letters)

botao = st.button("gerar")
if botao:
    st.text(f"A senha gerada foi: {aleatorio}")
print(tamanho)