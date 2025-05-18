import tkinter as tk

class WidgetFactory:
    @staticmethod
    def create_widget(widget_type, parent, **kwargs):
        if widget_type == "label":
            return tk.Label(parent, **kwargs)
        elif widget_type == "button":
            return tk.Button(parent, **kwargs)
        elif widget_type == "entry":
            return tk.Entry(parent, **kwargs)
        elif widget_type == "text":
            return tk.Text(parent, **kwargs)
        else:
            raise ValueError("Tipo de widget inválido")
