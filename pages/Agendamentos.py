import streamlit as st
import pandas as pd
import mysql.connector
import datetime

con = mysql.connector.connect(
host="26.87.213.126",
user="root",
password="clara02",
database="fisio_equilibrium")


st.set_page_config(page_title="Agendamentos", page_icon=":table:", layout="wide")
st.header("Equilibrium Fisioterapia e Pilates")
st.subheader("Agendamentos")

data = pd.read_sql("SELECT id, paciente, dia_semana, hora_inicio, hora_fim, quantidade  FROM agenda", conexao.con)
df = pd.DataFrame(data)

df_editavel = st.data_editor(df)

if st.button('Salvar'):
    cursor_update = conexao.con.cursor()
    update_agendamento = "UPDATE agenda SET paciente = %s, dia_semana = %s, quantidade = %s WHERE id = %s"
    quantidade = int(df_editavel.iloc[0]['quantidade'])
    id_agenda = int(df_editavel.iloc[0]['id'])
    cursor_update.execute(update_agendamento, (df_editavel.iloc[0]['paciente'], df_editavel.iloc[0]['dia_semana'], quantidade, id_agenda))
    conexao.con.commit()

    st.success("Agendamentos salvos com sucesso!")
