from .model import ChatBotModel
from .strategy import PalavraChaveStrategy

class ChatBotController:
    def __init__(self, respostas):
        self.modelo = ChatBotModel(respostas)
        self.estrategia = PalavraChaveStrategy()

    def processar_mensagem(self, mensagem):
        return self.modelo.encontrar_melhor_resposta(mensagem, self.estrategia)
