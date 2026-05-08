import streamlit as st

st.write("# Chatbot com IA")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []
#st.session_state




texto_usuario = st.chat_input("Digite sua mensagem aqui...")

for mensagen in st.session_state["lista_mensagens"]:
    role = mensagen["role"]
    content = mensagen["content"]
    if mensagen["role"] == "user":
        st.chat_message("user").write(mensagen["content"])
    else:
        st.chat_message("assistant").write(mensagen["content"])

if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)

    resposta_ia = "Você perguntou: " + texto_usuario

    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)

print(st.session_state["lista_mensagens"])