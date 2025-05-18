# text_area.py
import tkinter as tk

canvas = None  # canvas global para acesso externo

def create(root, theme):
    global canvas
    canvas = tk.Canvas(root, bg="white", width=500, height=400)
    canvas.pack(expand=tk.YES, fill=tk.BOTH)
    canvas.y = 20  # Inicializa a posição Y

def adicionar_mensagem(mensagem, remetente='user'):
    global canvas
    if not canvas:
        return
    
    cor = 'blue' if remetente == 'user' else 'green'
    x = 790 if remetente == 'user' else 20
    anchor = 'e' if remetente == 'user' else 'w'

    canvas.create_text(x, canvas.y, font=("Arial", 20), text=mensagem, anchor=anchor, tags='texto', fill=cor)
    canvas.y += 30
