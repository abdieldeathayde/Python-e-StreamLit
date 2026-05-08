import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ==========================================
# Carrega variáveis do ambiente
# ==========================================
load_dotenv()

# ==========================================
# Configuração da API Gemini
# ==========================================
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Modelo Gemini
modelo_ia = genai.GenerativeModel("models/gemini-2.0-flash-lite")

# ==========================================
# Configuração da página
# ==========================================
st.set_page_config(
    page_title="Chatbot Gemini",
    page_icon="🤖",
    layout="centered"
)

st.write("# 🤖 Chatbot com Gemini AI")

# ==========================================
# Histórico de mensagens
# ==========================================
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# ==========================================
# Exibe mensagens anteriores
# ==========================================
for mensagem in st.session_state["lista_mensagens"]:
    st.chat_message(mensagem["role"]).write(mensagem["content"])

# ==========================================
# Entrada do usuário
# ==========================================
texto_usuario = st.chat_input("Digite sua mensagem aqui...")

# ==========================================
# Processa mensagem
# ==========================================
if texto_usuario:

    # Exibe mensagem do usuário
    st.chat_message("user").write(texto_usuario)

    # Salva mensagem do usuário
    mensagem_usuario = {
        "role": "user",
        "content": texto_usuario
    }

    st.session_state["lista_mensagens"].append(mensagem_usuario)

    # ==========================================
    # Cria contexto da conversa
    # ==========================================
    contexto = ""

    for mensagem in st.session_state["lista_mensagens"]:
        contexto += f"{mensagem['role']}: {mensagem['content']}\n"

    # ==========================================
    # Resposta da IA
    # ==========================================
    with st.spinner("Pensando..."):

        resposta = modelo_ia.generate_content(contexto)

        texto_resposta_ia = resposta.text

    # Exibe resposta da IA
    st.chat_message("assistant").write(texto_resposta_ia)

    # Salva resposta da IA
    mensagem_ia = {
        "role": "assistant",
        "content": texto_resposta_ia
    }

    st.session_state["lista_mensagens"].append(mensagem_ia)