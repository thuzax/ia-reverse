class Tabuleiro:
    tabuleiro = None
    tamanho = None

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.montarTabuleiro()
        self.colocarPecasIniciais()

    def montarTabuleiro(self):
        self.tabuleiro = []
        for i in range(self.tamanho):
            self.tabuleiro.append([])
            for j in range(self.tamanho):
                self.tabuleiro[i].append("v")
        return self.tabuleiro

    def colocarPecasIniciais(self):
        linha1 = (self.tamanho - 1) // 2
        coluna1 = (self.tamanho - 1) // 2
        linha2 = (self.tamanho) // 2
        coluna2 = (self.tamanho) // 2

        self.tabuleiro[linha1][coluna1] = "B"
        self.tabuleiro[linha1][coluna2] = "P"
        self.tabuleiro[linha2][coluna1] = "P"
        self.tabuleiro[linha2][coluna2] = "B"

    def fazerJogada(self, jogador, linha, coluna):
        if(self.tabuleiro[linha][coluna] != "v"):
            return "ocupado"
        
        self.tabuleiro[linha][coluna] = jogador
        self.substituiVertical(jogador, linha, coluna)
        self.substituiHorizontal(jogador, linha, coluna)
        self.substituiDiagonal(jogador, linha, coluna)

    def substituiVertical(self, jogador, linha, coluna):
        self.substituiSubindo(jogador, linha, coluna)
        self.substituiDescendo(jogador, linha, coluna)
        
        return False

    def substituiSubindo(self, jogador, linha, coluna):
        if((linha <= 0) or (self.tabuleiro[linha-1][coluna] == "v")):
            return False
        
        if(self.tabuleiro[linha-1][coluna] != jogador):
            achou = self.substituiSubindo(jogador, linha - 1, coluna)
            
            if(achou):
                self.tabuleiro[linha-1][coluna] = jogador
            return achou

        elif(self.tabuleiro[linha-1][coluna] == jogador):
            return True

        return False

    def substituiDescendo(self, jogador, linha, coluna):
        if(linha >= (len(self.tabuleiro) - 1) or (self.tabuleiro[linha+1][coluna] == "v")):
            return False
        
        if(self.tabuleiro[linha+1][coluna] != jogador):
            achou = self.substituiDescendo(jogador, linha + 1, coluna)
            
            if(achou):
                self.tabuleiro[linha+1][coluna] = jogador
            return achou
        
        elif(self.tabuleiro[linha+1][coluna] == jogador):
            return True

        return False

    def substituiHorizontal(self, jogador, linha, coluna):
        self.substituiEsquerda(jogador, linha, coluna)
        self.substituiDireita(jogador, linha, coluna)


    def substituiEsquerda(self, jogador, linha, coluna):
        if((coluna <= 0) or (self.tabuleiro[linha][coluna-1] == "v")):
            return False

        if(self.tabuleiro[linha][coluna-1] != jogador):
            achou = self.substituiEsquerda(jogador, linha, coluna - 1)
            if(achou):
                self.tabuleiro[linha][coluna-1] = jogador
            return achou
        
        elif(self.tabuleiro[linha][coluna-1] == jogador):
            return True

        return False

    def substituiDireita(self, jogador, linha, coluna):
        if((coluna >= len(self.tabuleiro) - 1) or (self.tabuleiro[linha][coluna+1] == "v")):
            return False

        if(self.tabuleiro[linha][coluna+1] != jogador):
            achou = self.substituiDireita(jogador, linha, coluna + 1)
            if(achou):
                self.tabuleiro[linha][coluna+1] = jogador
            return achou
        
        elif(self.tabuleiro[linha][coluna+1] == jogador):
            return True

        return False

    def substituiDiagonal(self, jogador, linha, coluna):
        self.substituiDiagonalSubindoEsquerda(jogador, linha, coluna)
        self.substituiDiagonalDescendoDireita(jogador, linha, coluna)
        self.substituiDiagonalSubindoDireita(jogador, linha, coluna)
        self.substituiDiagonalDescendoEsquerda(jogador, linha, coluna)

    def substituiDiagonalSubindoEsquerda(self, jogador, linha, coluna):
        if((coluna <= 0) or (linha <= 0) or self.tabuleiro[linha-1][coluna-1] == "v"):
            return False
        
        if(self.tabuleiro[linha-1][coluna-1] != jogador):
            achou = self.substituiDiagonalSubindoEsquerda(jogador, linha - 1, coluna - 1)
            if(achou):
                self.tabuleiro[linha-1][coluna-1] = jogador
            return achou
        
        elif(self.tabuleiro[linha-1][coluna-1] == jogador):
            return True

        return False
        
    
    def substituiDiagonalDescendoDireita(self, jogador, linha, coluna):
        if((coluna >= (len(self.tabuleiro) - 1)) or (linha >= (len(self.tabuleiro) - 1)) 
                or self.tabuleiro[linha+1][coluna+1] == "v"):
            return False
        
        if(self.tabuleiro[linha+1][coluna+1] != jogador):
            achou = self.substituiDiagonalDescendoDireita(jogador, linha + 1, coluna + 1)
            if(achou):
                self.tabuleiro[linha+1][coluna+1] = jogador
            return achou
        
        elif(self.tabuleiro[linha+1][coluna+1] == jogador):
            return True

        return False
    
    def substituiDiagonalSubindoDireita(self, jogador, linha, coluna):
        if((coluna >= (len(self.tabuleiro) - 1)) or (linha <= 0) 
                or self.tabuleiro[linha-1][coluna+1] == "v"):
            return False
        if(self.tabuleiro[linha-1][coluna+1] != jogador):
            achou = self.substituiDiagonalSubindoDireita(jogador, linha - 1, coluna + 1)
            if(achou):
                self.tabuleiro[linha-1][coluna+1] = jogador
            return achou
        
        elif(self.tabuleiro[linha-1][coluna+1] == jogador):
            return True

        return False

    def substituiDiagonalDescendoEsquerda(self, jogador, linha, coluna):
        if((coluna <= 0) or (linha >= (len(self.tabuleiro) - 1)) 
                or self.tabuleiro[linha+1][coluna-1] == "v"):
            return False
        if(self.tabuleiro[linha+1][coluna-1] != jogador):
            achou = self.substituiDiagonalDescendoEsquerda(jogador, linha + 1, coluna - 1)
            if(achou):
                self.tabuleiro[linha+1][coluna-1] = jogador
            return achou
        
        elif(self.tabuleiro[linha+1][coluna-1] == jogador):
            return True

        return False


    def __str__(self):
        saida = "\t"

        for i in range(len(self.tabuleiro)):
            saida += str(i) + "\t"

        saida += "\n"

        for i in range(len(self.tabuleiro)):
            saida += str(i) + "\t"
            
            for j in range(len(self.tabuleiro)):
                saida += str(self.tabuleiro[i][j]) + "\t"
            
            saida += "\n"

        return saida
    