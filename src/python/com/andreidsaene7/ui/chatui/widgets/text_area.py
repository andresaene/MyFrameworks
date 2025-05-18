import tkinter as tk

def create(root, theme):
    chat_area = tk.Text(root, height=20, width=50, bg=theme.BG, fg=theme.FG)
    chat_area.pack(pady=10)
