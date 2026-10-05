import streamlit as st
import pandas as pd

st.title("Meu primeiro dash")
nome = "Enzo Barrêto Mello"
st.subheader(nome)
st.write("Olá, mundo")
idade = 18
st.write(f"Meu nome é {nome} e tenho {idade} anos.")

df = pd.DataFrame({
    "Matéria": ["Português", "Matemática", "Python", "Frame"],
    "Nota": [5, 9, 7, 10]
})
df

st.subheader("Compras de supermercado")
precos = {"Arroz (1 kg)": 6.00, "Feijão (1 kg)": 8.00,
          "Leite (1 L)": 5.00, "Pão (pacote)": 7.50,
          "Ovos (dúzia)": 12.00}

def calcular_preco_compra(item, quantidade):
    return precos[item] * quantidade

item = st.selectbox("Selecione um item de supermercado:", list(precos))
quantidade = st.number_input("Quantidade:", min_value=1, value=1, step=1)
total = calcular_preco_compra(item, quantidade)
st.write(f"Preço por unidade: R$ {precos[item]:.2f}".replace(".", ","))
st.metric("Preço da compra", f"R$ {total:.2f}".replace(".", ","))
