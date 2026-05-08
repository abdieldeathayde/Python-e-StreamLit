import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

st.write("# Chatbot com IA")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []
#st.session_state




texto_usuario = st.chat_input("Digite sua mensagem aqui...")

for mensagen in st.session_state["lista_mensagens"]:
    role = mensagen["role"]
    content = mensagen["content"]
    st.chat_message(role).write(content)
   

if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)

    #IA respondeu
    resposta_ia =  modelo_ia.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state["lista_mensagens"]
    )

    texto_resposta_ia = resposta_ia.choices[0].message.content
    resposta_ia = resposta_ia.choices[0].message

    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
