import tkinter as tk
from com.andreidsaene7.ui.chatui.widgets import button, entry, text_area

class ChatUIBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("400x500")
        self.root.configure(bg="white")
    
    def build(self):
        text_area.create(self.root)
        entry.create(self.root)
        button.create(self.root)

    
    