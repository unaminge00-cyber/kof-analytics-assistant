
import streamlit as st

st.title("🤖 KOF Analytics Assistant")

pregunta = st.chat_input("Pregunta algo...")

if pregunta:
    st.chat_message("user").write(pregunta)

    respuesta = "Respuesta desde Genie"

    st.chat_message("assistant").write(respuesta)
