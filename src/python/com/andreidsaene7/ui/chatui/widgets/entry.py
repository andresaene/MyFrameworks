# entry.py
import tkinter as tk

def create(root, theme):
    entrada = tk.Entry(root, font=("Arial", 20), width=50)
    entrada.pack(side=tk.LEFT, padx=10, pady=10)
    return entrada
