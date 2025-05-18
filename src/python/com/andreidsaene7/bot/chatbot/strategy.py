import re

class MatchingStrategy:
    def responder(self, mensagem, respostas):
        raise NotImplementedError

class PalavraChaveStrategy(MatchingStrategy):
    def responder(self, mensagem, respostas):
        melhor_resposta = 'Desculpe, não entendi essa pergunta.'
        melhor_pontuacao = 0
        palavras_mensagem = set(re.findall(r'\b\w+\b', mensagem.lower()))

        for pergunta, resposta in respostas.items():
            palavras_pergunta = set(re.findall(r'\b\w+\b', pergunta.lower()))
            pontuacao = len(palavras_pergunta.intersection(palavras_mensagem))
            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                melhor_resposta = resposta

        return melhor_resposta
