import tkinter as tk

def on_send():
    print("Mensagem enviada!")

def create(root, theme):
    send_button = tk.Button(root, text="Enviar", command=on_send, bg=theme.BG, fg=theme.FG)
    send_button.pack(side="bottom", pady=10)

