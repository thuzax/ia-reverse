class Tabuleiro:
    tabuleiro = None
    tamanho = None
    pontuacao = None
    quantidadeNaLinha = None
    quantidadeNaColuna = None

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.montarTabuleiro()
        
        self.quantidadeNaLinha = {"P" : [], "B" : []}
        self.quantidadeNaColuna = {"P" : [], "B" : []}
        for i in range(self.tamanho):
            self.quantidadeNaLinha["P"].append(0)
            self.quantidadeNaLinha["B"].append(0)
            self.quantidadeNaColuna["P"].append(0)
            self.quantidadeNaColuna["B"].append(0)
        
        print(self.quantidadeNaLinha)
        print(self.quantidadeNaColuna)
        self.colocarPecasIniciais()
        self.pontuacao = {"P": 2, "B": 2}


    def montarTabuleiro(self):
        self.tabuleiro = []
        for i in range(self.tamanho):
            self.tabuleiro.append([])
            for j in range(self.tamanho):
                self.tabuleiro[i].append("v")
        return self.tabuleiro

    def jogadaPossivel(self, jogador, linha, coluna):
        print(self.quantidadeNaLinha)
        print(self.quantidadeNaColuna)
        pass

    def colocarPecasIniciais(self):
        linha1 = (self.tamanho - 1) // 2
        coluna1 = (self.tamanho - 1) // 2
        linha2 = (self.tamanho) // 2
        coluna2 = (self.tamanho) // 2

        self.tabuleiro[linha1][coluna1] = "B"
        self.quantidadeNaLinha["B"][linha1] += 1
        self.quantidadeNaColuna["B"][coluna1] += 1
        
        self.tabuleiro[linha1][coluna2] = "P"
        self.quantidadeNaLinha["P"][linha1] += 1
        self.quantidadeNaColuna["P"][coluna2] += 1
        
        self.tabuleiro[linha2][coluna1] = "P"
        self.quantidadeNaLinha["P"][linha2] += 1
        self.quantidadeNaColuna["P"][coluna1] += 1
        
        self.tabuleiro[linha2][coluna2] = "B"
        self.quantidadeNaLinha["B"][linha2] += 1
        self.quantidadeNaColuna["B"][coluna2] += 1


    def fazerJogada(self, jogador, linha, coluna):
        if(self.tabuleiro[linha][coluna] != "v"):
            return "ocupado"
        
        self.tabuleiro[linha][coluna] = jogador
        self.pontuacao[jogador] += 1
        self.quantidadeNaLinha[jogador][linha] += 1
        self.quantidadeNaColuna[jogador][coluna] += 1

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
                self.quantidadeNaLinha[jogador][linha-1] += 1
                self.quantidadeNaColuna[jogador][coluna] += 1
                self.pontuacao[jogador] += 1

                self.pontuacao[outroJogador] -= 1
                self.quantidadeNaLinha[outroJogador][linha-1] -= 1
                self.quantidadeNaColuna[outroJogador][coluna] -= 1

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
    