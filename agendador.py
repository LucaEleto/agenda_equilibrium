import streamlit as st
import pandas as pd
import mysql.connector
import datetime

con = mysql.connector.connect(
host="localhost",
user="root",
password="clara02",
database="fisio_equilibrium")

st.set_page_config(page_title="Agendador", page_icon=":calendar:", layout="wide")
st.header("Equilibrium Fisioterapia e Pilates")
st.subheader("Agendamento")
paciente = st.text_input('Paciente:')
dia_semana = st.selectbox('Dias da Semana:', ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'])
hora_inicio = st.time_input('Horário Inicio:', step=datetime.timedelta(minutes=30))
hora_fim = st.time_input('Horario Fim:', step=datetime.timedelta(minutes=30))
quantidade = st.number_input('Aulas Semanais', min_value=1, max_value=3, step=1)

if st.button('Agendar'):
    inserir_sql = 'INSERT INTO agenda (paciente, dia_semana, hora_inicio, hora_fim, quantidade) VALUES (%s, %s, %s, %s, %s)'
    cursor = con.cursor()
    cursor.execute(inserir_sql, (paciente, dia_semana, hora_inicio, hora_fim, quantidade))
    con.commit()
    cursor.close()
    st.success("Agendamento realizado com sucesso!")
