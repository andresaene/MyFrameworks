import tkinter as tk
from com.andreidsaene7.ui.chatui.core.builder import ChatUIBuilder

def main():
    root = tk.Tk()
    ui = ChatUIBuilder(root)
    ui.build()
    root.mainloop()

if __name__ == "__main__":
    main()
