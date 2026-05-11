import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# carregar .env
load_dotenv()

# configurar Cliente Groq
# Certifique-se de ter a GROQ_API_KEY no seu arquivo .env
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# título
st.title("Chat com Groq (Llama 3)")

# memória do chat
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# exibir histórico
for mensagem in st.session_state["lista_mensagens"]:
    st.chat_message(mensagem["role"]).write(mensagem["content"])

# input usuário
mensagem_usuario = st.chat_input("Digite sua mensagem")

if mensagem_usuario:
    # mostrar mensagem usuário
    st.chat_message("user").write(mensagem_usuario)

    # salvar histórico (formato compatível com Groq/OpenAI)
    st.session_state["lista_mensagens"].append({
        "role": "user", 
        "content": mensagem_usuario
    })

    try:
        # Gerar resposta
        # Diferente do seu código anterior, não precisamos criar a string 'contexto' manualmente.
        # Passamos a lista de mensagens inteira para a API manter o contexto.
        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile", # Modelo potente e gratuito (checar modelos no console da Groq)
            messages=st.session_state["lista_mensagens"],
        )

        resposta_ia = chat_completion.choices[0].message.content

        # mostrar resposta
        st.chat_message("assistant").write(resposta_ia)

        # salvar resposta no histórico
        st.session_state["lista_mensagens"].append({
            "role": "assistant", 
            "content": resposta_ia
        })

    except Exception as erro:
        st.error(f"Erro na Groq: {erro}")