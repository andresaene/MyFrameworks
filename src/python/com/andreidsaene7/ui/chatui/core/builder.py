from com.andreidsaene7.ui.chatui.widgets import button, entry, text_area
from com.andreidsaene7.ui.chatui.core.factory import WidgetFactory


class ChatUIBuilder:
    def __init__(self, root, theme):
        self.root = root
        self.theme = theme
        self.root.title("Chatbot")
        self.root.geometry("850x500")
        self.root.configure(bg=self.theme.BG)

    def build(self):
        text_area.create(self.root, self.theme)
        entrada = entry.create(self.root, self.theme)
        button.create(self.root, self.theme, entrada)
