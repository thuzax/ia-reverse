class Tabuleiro:
    tabuleiro = None
    tamanho = None
    pontuacao = None
    posicaoPecas = None
    resultadoJogada = None

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.montarTabuleiro()
        self.posicaoPecas = {"P": [], "B": []}
        self.colocarPecasIniciais()
        self.pontuacao = {"P": 2, "B": 2}
        self.resultadoJogada = {}


    def montarTabuleiro(self):
        self.tabuleiro = []
        for i in range(self.tamanho):
            self.tabuleiro.append([])
            for j in range(self.tamanho):
                self.tabuleiro[i].append("v")
        return self.tabuleiro

    def pegarJogadasPossiveis(self, jogador):
        outroJogador = "P"
        if(jogador == "B"):
            outroJogador = "P"
        for posicaoPeca in self.posicaoPecas[jogador]:
            pass
            # self.pegaPecasViradasHorizontal(jogador, outroJogador,posicaoPeca[0], posicaoPeca[1])
        pass
                    

    def colocarPecasIniciais(self):
        linha1 = (self.tamanho - 1) // 2
        coluna1 = (self.tamanho - 1) // 2
        linha2 = (self.tamanho) // 2
        coluna2 = (self.tamanho) // 2

        self.tabuleiro[linha1][coluna1] = "B"
        self.posicaoPecas["B"].append((linha1, coluna1))
        
        self.tabuleiro[linha1][coluna2] = "P"
        self.posicaoPecas["P"].append((linha1, coluna2))
        
        self.tabuleiro[linha2][coluna1] = "P"
        self.posicaoPecas["P"].append((linha2, coluna1))
        
        self.tabuleiro[linha2][coluna2] = "B"
        self.posicaoPecas["B"].append((linha2, coluna2))


    def fazerJogada(self, jogador, linha, coluna):
        if(self.tabuleiro[linha][coluna] != "v"):
            return "ocupado"
        
        self.tabuleiro[linha][coluna] = jogador
        self.pontuacao[jogador] += 1

        outroJogador = "P" if(jogador == "B") else "B"

        
    def pegaPecasViradasVertical(self, jogador, outroJogador, linha, coluna):
        retornoSubindo = self.pegaPecasViradasSubindo(jogador, outroJogador, linha, coluna)
        if(retornoSubindo == None):
            retornoSubindo = []
        else:
            self.resultadoJogada[retornoSubindo["posicao"]] = retornoSubindo["pecasViradas"]
            
        
        retornoDescendo = self.pegaPecasViradasDescendo(jogador, outroJogador, linha, coluna)
        if(retornoDescendo == None):
            retornoDescendo = []
        else:
            self.resultadoJogada[retornoDescendo["posicao"]] = retornoSubindo["pecasViradas"]
        

    def pegaPecasViradasSubindo(self, jogador, outroJogador, linha, coluna):
        if((linha <= 0) or self.tabuleiro[linha-1][coluna] == jogador):
            return None
        
        if(self.tabuleiro[linha-1][coluna] == outroJogador):
            resultadoJogada = self.pegaPecasViradasSubindo(jogador, outroJogador, linha - 1, coluna)
            
            if(resultadoJogada != None):
                resultadoJogada["pecasViradas"].append((linha - 1, coluna))
            return resultadoJogada

        elif(self.tabuleiro[linha-1][coluna] == "v"):
            return {"posicao": (linha-1, coluna), "pecasViradas": []}

        return None

    def pegaPecasViradasDescendo(self, jogador, outroJogador, linha, coluna):
        if(linha >= (len(self.tabuleiro) - 1) or (self.tabuleiro[linha+1][coluna] == jogador)):
            return None
        
        if(self.tabuleiro[linha+1][coluna] == outroJogador):
            resultadoJogada = self.pegaPecasViradasDescendo(jogador, outroJogador, linha + 1, coluna)
            
            if(resultadoJogada != None):
                resultadoJogada["pecasViradas"].append((linha + 1, coluna))
            return resultadoJogada
        
        elif(self.tabuleiro[linha+1][coluna] == "v"):
            return {"posicao": (linha+1, coluna), "pecasViradas": []}

        return None

    def pegaPecasViradasHorizontal(self, jogador, outroJogador, linha, coluna):
        retornoEsquerda = self.pegaPecasViradasEsquerda(jogador, outroJogador, linha, coluna)
        if(retornoEsquerda == None):
            retornoEsquerda = []
        else:
            self.resultadoJogada[retornoEsquerda["posicao"]] = retornoEsquerda["pecasViradas"]

        retornoDireita = self.pegaPecasViradasDireita(jogador, outroJogador, linha, coluna)
        if(retornoDireita == None):
            retornoDireita = []
        else:
            self.resultadoJogada[retornoDireita["posicao"]] = retornoDireita["pecasViradas"]


    def pegaPecasViradasEsquerda(self, jogador, outroJogador, linha, coluna):
        if((coluna <= 0) or (self.tabuleiro[linha][coluna-1] == jogador)):
            return None

        if(self.tabuleiro[linha][coluna-1] == outroJogador):
            resultadoJogada = self.pegaPecasViradasEsquerda(jogador, outroJogador, linha, coluna - 1)
            if(resultadoJogada != None):
                resultadoJogada["pecasValidas"].append((linha, coluna - 1))
            return resultadoJogada
        
        elif(self.tabuleiro[linha][coluna-1] == "v"):
            return {"posicao": (linha, coluna-1), "pecasViradas": []}

        return None

    def pegaPecasViradasDireita(self, jogador, outroJogador, linha, coluna):
        if((coluna >= len(self.tabuleiro) - 1) or (self.tabuleiro[linha][coluna+1] == jogador)):
            return None

        if(self.tabuleiro[linha][coluna+1] == outroJogador):
            resultadoJogada = self.pegaPecasViradasDireita(jogador, outroJogador, linha, coluna + 1)
            if(resultadoJogada != None):
                resultadoJogada["pecasValidas"].append((linha, coluna + 1))
            return resultadoJogada
        
        elif(self.tabuleiro[linha][coluna+1] == "v"):
            return {"posicao": (linha, coluna+1), "pecasViradas": []}

        return None

    def pegaPecasViradasDiagonal(self, jogador, outroJogador, linha, coluna):
        retornoSubindoEsquerda = self.pegaPecasViradasDiagonalSubindoEsquerda(jogador, outroJogador, linha, coluna)
        if(retornoSubindoEsquerda == None):
            retornoSubindoEsquerda = []
        else:
            self.resultadoJogada[retornoSubindoEsquerda["posicao"]] = retornoSubindoEsquerda["pecasViradas"]

        retornoSubindoDireita = self.pegaPecasViradasDiagonalSubindoDireita(jogador, outroJogador, linha, coluna)
        if(retornoSubindoDireita == None):
            retornoSubindoDireita = []
        else:
            self.resultadoJogada[retornoSubindoDireita["posicao"]] = retornoSubindoDireita["pecasViradas"]

        retornoDescendoEsquerda = self.pegaPecasViradasDiagonalDescendoEsquerda(jogador, outroJogador, linha, coluna)
        if(retornoDescendoEsquerda == None):
            retornoDescendoEsquerda = []
        else:
            self.resultadoJogada[retornoDescendoEsquerda["posicao"]] = retornoDescendoEsquerda["pecasViradas"]

        retornoDescendoDireita = self.pegaPecasViradasDiagonalDescendoDireita(jogador, outroJogador, linha, coluna)
        if(retornoDescendoDireita == None):
            retornoDescendoDireita = []
        else:
            self.resultadoJogada[retornoDescendoDireita["posicao"]] = retornoDescendoDireita["pecasViradas"]
        
    def pegaPecasViradasDiagonalSubindoEsquerda(self, jogador, outroJogador, linha, coluna):
        if((coluna <= 0) or (linha <= 0) or self.tabuleiro[linha-1][coluna-1] == jogador):
            return None
        
        if(self.tabuleiro[linha-1][coluna-1] == outroJogador):
            resultadoJogada = self.pegaPecasViradasDiagonalSubindoEsquerda(jogador, outroJogador, linha - 1, coluna - 1)
            if(resultadoJogada != None):
                resultadoJogada["pecasViradas"].append((linha - 1, coluna - 1))
            return resultadoJogada
        
        elif(self.tabuleiro[linha-1][coluna-1] == "v"):
            return {"posicao": (linha-1, coluna-1), "pecasViradas": []}

        return None
        
    
    def pegaPecasViradasDiagonalDescendoDireita(self, jogador, outroJogador, linha, coluna):
        if((coluna >= (len(self.tabuleiro) - 1)) or (linha >= (len(self.tabuleiro) - 1)) 
                or self.tabuleiro[linha+1][coluna+1] == jogador):
            return None
        
        if(self.tabuleiro[linha+1][coluna+1] == outroJogador):
            resultadoJogada = self.pegaPecasViradasDiagonalDescendoDireita(jogador, outroJogador, linha + 1, coluna + 1)
            if(resultadoJogada != None):
                resultadoJogada["pecasViradas"].append((linha + 1, coluna + 1))
            return resultadoJogada
        
        elif(self.tabuleiro[linha+1][coluna+1] == "v"):
            return {"posicao": (linha+1, coluna+1), "pecasViradas": []}

        return None
    
    def pegaPecasViradasDiagonalSubindoDireita(self, jogador, outroJogador, linha, coluna):
        if((coluna >= (len(self.tabuleiro) - 1)) or (linha <= 0) 
                or self.tabuleiro[linha-1][coluna+1] == jogador):
            return None
        if(self.tabuleiro[linha-1][coluna+1] == outroJogador):
            resultadoJogada = self.pegaPecasViradasDiagonalSubindoDireita(jogador, outroJogador, linha - 1, coluna + 1)
            if(resultadoJogada != None):
                resultadoJogada["pecasViradas"].append((linha - 1, coluna + 1))
            return resultadoJogada
        
        elif(self.tabuleiro[linha-1][coluna+1] == "v"):
            return {"posicao": (linha-1, coluna+1), "pecasViradas": []}

        return None

    def pegaPecasViradasDiagonalDescendoEsquerda(self, jogador, outroJogador, linha, coluna):
        if((coluna <= 0) or (linha >= (len(self.tabuleiro) - 1)) 
                or self.tabuleiro[linha+1][coluna-1] == jogador):
            return None
        if(self.tabuleiro[linha+1][coluna-1] == outroJogador):
            resultadoJogada = self.pegaPecasViradasDiagonalDescendoEsquerda(jogador, outroJogador, linha + 1, coluna - 1)
            if(resultadoJogada != None):
                resultadoJogada["pecasViradas"].append((linha + 1, coluna - 1))
            return resultadoJogada
        
        elif(self.tabuleiro[linha+1][coluna-1] == "v"):
            return {"posicao": (linha+1, coluna-1), "pecasViradas": []}

        return None


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
    