import streamlit as st
import conexao

st.set_page_config(page_title="Login", page_icon=":lock:", layout="wide")

st.title("Equilibrium Fisioterapia e Pilates")
st.subheader("Login")

usuario = st.text_input('Usuário')
senha = st.text_input('Senha', type="password")
if st.button('Entrar'):
    if usuario == 'admin' and senha == 'admin':
        st.success("Login realizado com sucesso!")
        st.write("Bem-vindo, administrador!")
        st.link_button('Agendador',url='agendador.py')

    else:
        st.error("Usuário ou senha inválidos")