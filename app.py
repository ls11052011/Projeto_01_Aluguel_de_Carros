import streamlit as st 
st.title(" Ls Motores - Alugueis de Carro")
st.sidebar.title("Escolha seu modelo")
st.sidebar.image('logo.png')

carros = ['BMW', 'Porshe', 'Fusca', 'Toro']

opcao = st. sidebar.selectbox('Escolha o carro que vai ser alugado', carros)

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou modelo: {opcao}')
st.markdown('---')

dias = st. number_input('Quantos dias você vai alugar o carro?', min_value=1, step=1)
km = st. text_input('Quantos km voce vai rodar?')

if opcao == 'BMW':
    diaria = 120
elif opcao == 'Porshe':
    diaria = 250
elif opcao == 'Fusca':
    diaria = 80
elif opcao == 'Toro':
    diaria = 100



if st. button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.50   
    aluguel_total = total_dias+total_km
    st.warning(f' você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')   