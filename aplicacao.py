import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

# Obtém chave da API
api_key = os.getenv("XAI_API_KEY")

# Verifica se a chave existe
if not api_key:
    st.error("Chave XAI_API_KEY não encontrada no arquivo .env")
    st.stop()

# Cliente Grok
client = OpenAI(
    api_key=api_key,
    base_url="https://api.x.ai/v1"
)

# Configuração da página
st.set_page_config(
    page_title="Chat com Grok",
    page_icon="🤖"
)

st.title("Chat com Grok")

# Campo de entrada
pergunta = st.text_input("Digite sua pergunta")

# Envia pergunta
if pergunta:

    try:
        resposta = client.chat.completions.create(
            model="grok-3",
            messages=[
                {
                    "role": "user",
                    "content": pergunta
                }
            ],
            temperature=0.7,
            max_tokens=500
        )

        resposta_texto = resposta.choices[0].message.content

        st.write(resposta_texto)

    except Exception as e:
        st.error(f"Erro na API: {e}")