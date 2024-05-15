#streamlit run C:\Jhan\Desenvolvimento\Python\Codigo-Py\StreamLit\Basico\crud.py
import streamlit as st

st.title('Incluir Cliente')

with st.form(key = 'Incluir_Cliente '):
    nome = st.text_input(label=':blue[Nome:]')
    idade = st.number_input(label=':blue[Idade:]',format='%i', step=1)
    profissao = st.selectbox(label=':blue[Profissão:]',options=['Mecânico','Médico','Engenheiro','Dentista','Advogado','Arquiteto'])
    gravar = st.form_submit_button(':blue[Gravar:]')

if gravar:
    st.write(f'Nome: {nome}')
    st.write(f'idade: {idade}')
    st.write(f'profissao: {profissao}')
    
    aa = {f'nome: {nome}, idade: {idade}, profissao: {profissao}'}
    
    st.text(aa)
    
    
