import tkinter as tk

def create(root, theme):
    entry_field = tk.Entry(root, width=40, bg=theme.BG, fg=theme.FG)
    entry_field.pack(side="bottom", pady=5)
