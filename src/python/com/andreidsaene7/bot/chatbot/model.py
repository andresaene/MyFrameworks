import re

class ChatBotModel:
    def __init__(self, respostas):
        self.respostas = respostas

    def encontrar_melhor_resposta(self, mensagem, estrategia):
        return estrategia.responder(mensagem, self.respostas)
