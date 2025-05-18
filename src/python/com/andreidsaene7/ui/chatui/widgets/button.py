import tkinter as tk

def on_send():
    print("Mensagem enviada!")

def create(root):
    send_button = tk.Button(root, text="Enviar", command=on_send)
    send_button.pack(side="bottom", pady=10)
