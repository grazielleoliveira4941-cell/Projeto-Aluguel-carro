import streamlit as st
from datetime import datetime


st.title ("locadora e veiculo ")
carro = st. sidebar.selectbox("selecione o seu veículo:", ["Fusca","HB20", "GOLF","CIVIC","KOMBI","DOD RAM","MAVERICK","ESTÁDIO DO PALMEIRA"])
valores_diarias = {"Fusca": 250.00, "HB20":50.00, "GOLF":450.00,"CIVIC":550.00, "DOD RAM":50000.00,"MAVERICK":650.00,"KOMBI":248.00, "ESTÁDIO DO PALMEIRA":350.00} #DICÍONARIO

st.subheader(f"carro selecionado:{carro}\npreço da diária:{valores_diarias[carro]}")
st.image(f"{carro}.jpg", width= 500)

valor_diaria = valores_diarias[carro]

data_inicio = st.datetime_input("selecione o dia da retirada", datetime.now())
data_final = st.datetime_input("selecione o dia da devolução", data_inicio)


if st. button("calcular"): # se alguém clicar no botão
    dias = (data_final - data_inicio).days
    valor_total = valor_diaria * dias 
    st.subheader(f"Alugando{carro} por {dias} dias, o valor será: {valor_total:.2f}")

