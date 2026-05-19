import streamlit as st 
st.title(" Ls Motores - Alugueis de Carro")
st.sidebar.title("Escolha seu modelo")
st.sidebar.image('logo.png')

carros = [' BMW ', ' Porshe ', ' Fusca', ' Toro ']

opcao = st. sidebar.selectbox('escolha o carro que vai ser alugado', carros)

st. image(f'{opcao}.png')
st.markdown(f'## Voce alugouo modelo: {opcao}')
st.markdown('---')