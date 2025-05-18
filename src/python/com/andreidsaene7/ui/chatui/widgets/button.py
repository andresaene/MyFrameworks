# button.py
import tkinter as tk
from ....bot.chatbot.factory import criar_chatbot_padrao
from . import text_area  # importa seu canvas modularizado

chatbot = criar_chatbot_padrao()

def on_send(mensagem_usuario, entrada):
    if not mensagem_usuario.strip():
        return

    text_area.adicionar_mensagem(mensagem_usuario, remetente='user')

    resposta = chatbot.processar_mensagem(mensagem_usuario)
    text_area.adicionar_mensagem(resposta, remetente='bot')

    entrada.delete(0, tk.END)

def create(root, theme, entrada):
    send_button = tk.Button(
        root,
        text="Enviar",
        command=lambda: on_send(entrada.get(), entrada),
        bg=theme.BG,
        fg=theme.FG
    )
    send_button.pack(side="bottom", pady=10)
