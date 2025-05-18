from .controller import ChatBotController

def criar_chatbot_padrao():
    respostas = {
        'bom dia': 'Bom dia! Como posso ajudá-lo?',
        'tchau': 'Tchau! Foi bom conversar com você.',
        'como você está': 'Estou funcionando conforme programado. E você?',
        # ... outras respostas ...
    }
    return ChatBotController(respostas)
