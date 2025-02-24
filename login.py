import streamlit as st
import conexao

st.set_page_config(page_title="Login", page_icon=":lock:", layout="wide")

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("logo-1.png", width=200)

with col3:
    st.write('')
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.header("Equilibrium Fisioterapia e Pilates")

with col3:
    st.write('')


usuario = st.text_input('Usuário')
senha = st.text_input('Senha', type="password")
if st.button('Entrar'):
    if usuario == 'admin' and senha == 'admin':
        st.success("Login realizado com sucesso!")
        st.write("Bem-vindo, administrador!")
        st.link_button('Agendador',url='agendador.py')

    else:
        st.error("Usuário ou senha inválidos")