class Noh:
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro
        self.filhos = []
        self.pai = None
        self.ganho = None
        self.jogada = None