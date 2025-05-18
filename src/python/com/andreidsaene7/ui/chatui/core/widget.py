class BaseWidget:
    def __init__(self, widget):
        self.widget = widget

    def show(self):
        self.widget.pack(pady=5, padx=10)
