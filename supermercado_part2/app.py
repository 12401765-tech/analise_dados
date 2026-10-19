import streamlit as st
import pandas as pd

st.set_page_config(page_title="Supermercado",layout="centered")

st.title("Continuação do supermercado")

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

st.subheader("Calculadora de troco")
col1, col2 = st.columns(2)

with col1:
    valor_compra = st.number_input("Valor da compra (R$)", value=float(total), step=0.50, min_value=0.0)

with col2:
    valor_pago = st.number_input("Valor pago em dinheiro (R$)", value=0.0, step=1.0, min_value=0.0)

if st.button("Calcular troco", type="primary"):
    resultado = None
    if valor_pago < valor_compra:
        falta = valor_compra - valor_pago
        st.error(f"Pagamento insuficiente! Faltam R$ {falta:.2f}".replace(".", ","))
    else:
        resultado = round(valor_pago - valor_compra, 2)

    if resultado is not None:
        st.success(f"**Troco:** R$ {resultado:.2f}".replace(".", ","))
