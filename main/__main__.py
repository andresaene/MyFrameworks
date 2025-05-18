import tkinter as tk
from com.andreidsaene7.ui.chatui.core.builder import ChatUIBuilder
from com.andreidsaene7.ui.chatui.themes.dark import DarkTheme
# ou: from com.andreidsaene7.ui.chatui.themes.light import LightTheme

if __name__ == "__main__":
    root = tk.Tk()
    builder = ChatUIBuilder(root, theme=DarkTheme)
    builder.build()
    root.mainloop()
