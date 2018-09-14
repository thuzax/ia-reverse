class Tabuleiro:
    tabuleiro = None
    tamanho = None
    pontuacao = None

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.montarTabuleiro()
        self.colocarPecasIniciais()
        self.pontuacao = {"P": 2, "B": 2}

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
        self.pontuacao[jogador] += 1
        outroJogador = "P" if(jogador == "B") else "B"
        
        self.substituiVertical(jogador, outroJogador, linha, coluna)
        self.substituiHorizontal(jogador, outroJogador, linha, coluna)
        self.substituiDiagonal(jogador, outroJogador, linha, coluna)

    def substituiVertical(self, jogador, outroJogador, linha, coluna):
        self.substituiSubindo(jogador, outroJogador, linha, coluna)
        self.substituiDescendo(jogador, outroJogador, linha, coluna)
        
        return False

    def substituiSubindo(self, jogador, outroJogador, linha, coluna):
        if((linha <= 0) or (self.tabuleiro[linha-1][coluna] == "v")):
            return False
        
        if(self.tabuleiro[linha-1][coluna] == outroJogador):
            achou = self.substituiSubindo(jogador, outroJogador, linha - 1, coluna)
            
            if(achou):
                self.tabuleiro[linha-1][coluna] = jogador
                self.pontuacao[jogador] += 1
                self.pontuacao[outroJogador] -= 1
            return achou

        elif(self.tabuleiro[linha-1][coluna] == jogador):
            return True

        return False

    def substituiDescendo(self, jogador, outroJogador, linha, coluna):
        if(linha >= (len(self.tabuleiro) - 1) or (self.tabuleiro[linha+1][coluna] == "v")):
            return False
        
        if(self.tabuleiro[linha+1][coluna] == outroJogador):
            achou = self.substituiDescendo(jogador, outroJogador, linha + 1, coluna)
            
            if(achou):
                self.tabuleiro[linha+1][coluna] = jogador
                self.pontuacao[jogador] += 1
                self.pontuacao[outroJogador] -= 1
            return achou
        
        elif(self.tabuleiro[linha+1][coluna] == jogador):
            return True

        return False

    def substituiHorizontal(self, jogador, outroJogador, linha, coluna):
        self.substituiEsquerda(jogador, outroJogador, linha, coluna)
        self.substituiDireita(jogador, outroJogador, linha, coluna)


    def substituiEsquerda(self, jogador, outroJogador, linha, coluna):
        if((coluna <= 0) or (self.tabuleiro[linha][coluna-1] == "v")):
            return False

        if(self.tabuleiro[linha][coluna-1] == outroJogador):
            achou = self.substituiEsquerda(jogador, outroJogador, linha, coluna - 1)
            if(achou):
                self.tabuleiro[linha][coluna-1] = jogador
                self.pontuacao[jogador] += 1
                self.pontuacao[outroJogador] -= 1
            return achou
        
        elif(self.tabuleiro[linha][coluna-1] == jogador):
            return True

        return False

    def substituiDireita(self, jogador, outroJogador, linha, coluna):
        if((coluna >= len(self.tabuleiro) - 1) or (self.tabuleiro[linha][coluna+1] == "v")):
            return False

        if(self.tabuleiro[linha][coluna+1] == outroJogador):
            achou = self.substituiDireita(jogador, outroJogador, linha, coluna + 1)
            if(achou):
                self.tabuleiro[linha][coluna+1] = jogador
                self.pontuacao[jogador] += 1
                self.pontuacao[outroJogador] -= 1
            return achou
        
        elif(self.tabuleiro[linha][coluna+1] == jogador):
            return True

        return False

    def substituiDiagonal(self, jogador, outroJogador, linha, coluna):
        self.substituiDiagonalSubindoEsquerda(jogador, outroJogador, linha, coluna)
        self.substituiDiagonalDescendoDireita(jogador, outroJogador, linha, coluna)
        self.substituiDiagonalSubindoDireita(jogador, outroJogador, linha, coluna)
        self.substituiDiagonalDescendoEsquerda(jogador, outroJogador, linha, coluna)

    def substituiDiagonalSubindoEsquerda(self, jogador, outroJogador, linha, coluna):
        if((coluna <= 0) or (linha <= 0) or self.tabuleiro[linha-1][coluna-1] == "v"):
            return False
        
        if(self.tabuleiro[linha-1][coluna-1] == outroJogador):
            achou = self.substituiDiagonalSubindoEsquerda(jogador, outroJogador, linha - 1, coluna - 1)
            if(achou):
                self.tabuleiro[linha-1][coluna-1] = jogador
                self.pontuacao[jogador] += 1
                self.pontuacao[outroJogador] -= 1
            return achou
        
        elif(self.tabuleiro[linha-1][coluna-1] == jogador):
            return True

        return False
        
    
    def substituiDiagonalDescendoDireita(self, jogador, outroJogador, linha, coluna):
        if((coluna >= (len(self.tabuleiro) - 1)) or (linha >= (len(self.tabuleiro) - 1)) 
                or self.tabuleiro[linha+1][coluna+1] == "v"):
            return False
        
        if(self.tabuleiro[linha+1][coluna+1] == outroJogador):
            achou = self.substituiDiagonalDescendoDireita(jogador, outroJogador, linha + 1, coluna + 1)
            if(achou):
                self.tabuleiro[linha+1][coluna+1] = jogador
                self.pontuacao[jogador] += 1
                self.pontuacao[outroJogador] -= 1
            return achou
        
        elif(self.tabuleiro[linha+1][coluna+1] == jogador):
            return True

        return False
    
    def substituiDiagonalSubindoDireita(self, jogador, outroJogador, linha, coluna):
        if((coluna >= (len(self.tabuleiro) - 1)) or (linha <= 0) 
                or self.tabuleiro[linha-1][coluna+1] == "v"):
            return False
        if(self.tabuleiro[linha-1][coluna+1] == outroJogador):
            achou = self.substituiDiagonalSubindoDireita(jogador, outroJogador, linha - 1, coluna + 1)
            if(achou):
                self.tabuleiro[linha-1][coluna+1] = jogador
                self.pontuacao[jogador] += 1
                self.pontuacao[outroJogador] -= 1
            return achou
        
        elif(self.tabuleiro[linha-1][coluna+1] == jogador):
            return True

        return False

    def substituiDiagonalDescendoEsquerda(self, jogador, outroJogador, linha, coluna):
        if((coluna <= 0) or (linha >= (len(self.tabuleiro) - 1)) 
                or self.tabuleiro[linha+1][coluna-1] == "v"):
            return False
        if(self.tabuleiro[linha+1][coluna-1] == outroJogador):
            achou = self.substituiDiagonalDescendoEsquerda(jogador, outroJogador, linha + 1, coluna - 1)
            if(achou):
                self.tabuleiro[linha+1][coluna-1] = jogador
                self.pontuacao[jogador] += 1
                self.pontuacao[outroJogador] -= 1
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
    