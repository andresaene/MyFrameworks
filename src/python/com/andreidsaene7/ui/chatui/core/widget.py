from abc import ABC, abstractmethod

class BaseWidget(ABC):
    def __init__(self, root, theme):
        self.root = root
        self.theme = theme
        self.widget = None

    @abstractmethod
    def create_widget(self):
        pass

    def render(self):
        self.create_widget()
        self.widget.pack(pady=5, padx=10)

