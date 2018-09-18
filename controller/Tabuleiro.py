class Tabuleiro:

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabuleiro = []
        self.montarTabuleiro()
        self.posicaoPecas = {"P": [], "B": []}
        self.colocarPecasIniciais()
        self.pontuacao = {"P": 2, "B": 2}


    def montarTabuleiro(self):
        for i in range(self.tamanho):
            self.tabuleiro.append([])
            for j in range(self.tamanho):
                self.tabuleiro[i].append("-")
        return self.tabuleiro


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


    def pegaJogadasPossiveis(self, jogador, outroJogador):
        resultadoJogada = {}
        for peca in self.posicaoPecas[jogador]:
            self.pegaPecasViradasHorizontal(jogador, outroJogador, peca[0], peca[1], resultadoJogada)
            self.pegaPecasViradasVertical(jogador, outroJogador, peca[0], peca[1], resultadoJogada)
            self.pegaPecasViradasDiagonal(jogador, outroJogador, peca[0], peca[1], resultadoJogada)
        
        return resultadoJogada


    def viraPecas(self, jogador, outroJogador, posicoesPeca):
        self.tabuleiro[posicoesPeca[0]][posicoesPeca[1]] = jogador
        self.posicaoPecas[outroJogador].remove(posicoesPeca)
        self.posicaoPecas[jogador].append(posicoesPeca)
        self.pontuacao[jogador] += 1
        self.pontuacao[outroJogador] -= 1


    def fazerJogada(self, jogador, linha, coluna):
        outroJogador = "P" if(jogador == "B") else "B"

        
        resultadoJogada = self.pegaJogadasPossiveis(jogador, outroJogador)

        if((linha, coluna) not in resultadoJogada):
            return False
        
        
        self.tabuleiro[linha][coluna] = jogador
        self.posicaoPecas[jogador].append((linha, coluna))
        self.pontuacao[jogador] += 1
        for posicoesPeca in resultadoJogada[(linha, coluna)]:
            self.viraPecas(jogador, outroJogador, posicoesPeca)

        return True

    def pegaPecasViradasVertical(self, jogador, outroJogador, linha, coluna, resultadoJogada):
        retornoSubindo = self.pegaPecasViradasSubindo(jogador, outroJogador, linha, coluna)
        if(retornoSubindo != None):
            try:
                if(len(retornoSubindo["pecasViradas"]) > 0):
                    resultadoJogada[retornoSubindo["posicao"]] += retornoSubindo["pecasViradas"]
            except:
                resultadoJogada[retornoSubindo["posicao"]] = retornoSubindo["pecasViradas"]

        retornoDescendo = self.pegaPecasViradasDescendo(jogador, outroJogador, linha, coluna)
        if(retornoDescendo != None):
            try:
                if(len(retornoDescendo["pecasViradas"]) > 0):
                    resultadoJogada[retornoDescendo["posicao"]] += retornoDescendo["pecasViradas"]
            except:
                resultadoJogada[retornoDescendo["posicao"]] = retornoDescendo["pecasViradas"]


    def pegaPecasViradasSubindo(self, jogador, outroJogador, linha, coluna):
        if((linha <= 0) or self.tabuleiro[linha-1][coluna] == jogador):
            return None
        
        if(self.tabuleiro[linha-1][coluna] == outroJogador):
            resultadoJogada = self.pegaPecasViradasSubindo(jogador, outroJogador, linha - 1, coluna)
            
            if(resultadoJogada != None):
                resultadoJogada["pecasViradas"].append((linha - 1, coluna))
            return resultadoJogada

        elif(self.tabuleiro[linha-1][coluna] == "-"):
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
        
        elif(self.tabuleiro[linha+1][coluna] == "-"):
            return {"posicao": (linha+1, coluna), "pecasViradas": []}

        return None

    def pegaPecasViradasHorizontal(self, jogador, outroJogador, linha, coluna, resultadoJogada):
        retornoEsquerda = self.pegaPecasViradasEsquerda(jogador, outroJogador, linha, coluna)

        if(retornoEsquerda != None):
            try:
                if(len(retornoEsquerda["pecasViradas"]) > 0):
                    resultadoJogada[retornoEsquerda["posicao"]] += retornoEsquerda["pecasViradas"]
            except:
                resultadoJogada[retornoEsquerda["posicao"]] = retornoEsquerda["pecasViradas"]

        retornoDireita = self.pegaPecasViradasDireita(jogador, outroJogador, linha, coluna)
        if(retornoDireita != None):
            try:
                if(len(retornoDireita["pecasViradas"]) > 0):
                    resultadoJogada[retornoDireita["posicao"]] += retornoDireita["pecasViradas"]
            except:
                resultadoJogada[retornoDireita["posicao"]] = retornoDireita["pecasViradas"]

    def pegaPecasViradasEsquerda(self, jogador, outroJogador, linha, coluna):
        if((coluna <= 0) or (self.tabuleiro[linha][coluna-1] == jogador)):
            return None

        if(self.tabuleiro[linha][coluna-1] == outroJogador):
            resultadoJogada = self.pegaPecasViradasEsquerda(jogador, outroJogador, linha, coluna - 1)
            if(resultadoJogada != None):
                resultadoJogada["pecasViradas"].append((linha, coluna - 1))
            return resultadoJogada
        
        elif(self.tabuleiro[linha][coluna-1] == "-"):
            return {"posicao": (linha, coluna-1), "pecasViradas": []}

        return None

    def pegaPecasViradasDireita(self, jogador, outroJogador, linha, coluna):
        if((coluna >= len(self.tabuleiro) - 1) or (self.tabuleiro[linha][coluna+1] == jogador)):
            return None

        if(self.tabuleiro[linha][coluna+1] == outroJogador):
            resultadoJogada = self.pegaPecasViradasDireita(jogador, outroJogador, linha, coluna + 1)
            if(resultadoJogada != None):
                resultadoJogada["pecasViradas"].append((linha, coluna + 1))
            return resultadoJogada
        
        elif(self.tabuleiro[linha][coluna+1] == "-"):
            return {"posicao": (linha, coluna+1), "pecasViradas": []}

        return None

    def pegaPecasViradasDiagonal(self, jogador, outroJogador, linha, coluna, resultadoJogada):
        retornoSubindoEsquerda = self.pegaPecasViradasDiagonalSubindoEsquerda(jogador, outroJogador, linha, coluna)
        if(retornoSubindoEsquerda != None):
            try:
                if(len(retornoSubindoEsquerda["pecasViradas"]) > 0):
                    resultadoJogada[retornoSubindoEsquerda["posicao"]] += retornoSubindoEsquerda["pecasViradas"]
            except:
                resultadoJogada[retornoSubindoEsquerda["posicao"]] = retornoSubindoEsquerda["pecasViradas"]
            

        retornoSubindoDireita = self.pegaPecasViradasDiagonalSubindoDireita(jogador, outroJogador, linha, coluna)
        if(retornoSubindoDireita != None):
            try:
                if(len(retornoSubindoDireita["pecasViradas"]) > 0):
                    resultadoJogada[retornoSubindoDireita["posicao"]] += retornoSubindoDireita["pecasViradas"]
            except:
                resultadoJogada[retornoSubindoDireita["posicao"]] = retornoSubindoDireita["pecasViradas"]
            

        retornoDescendoEsquerda = self.pegaPecasViradasDiagonalDescendoEsquerda(jogador, outroJogador, linha, coluna)
        if(retornoDescendoEsquerda != None):
            try:
                if(len(retornoDescendoEsquerda["pecasViradas"]) > 0):
                    resultadoJogada[retornoDescendoEsquerda["posicao"]] += retornoDescendoEsquerda["pecasViradas"]
            except:
                resultadoJogada[retornoDescendoEsquerda["posicao"]] = retornoDescendoEsquerda["pecasViradas"]
            

        retornoDescendoDireita = self.pegaPecasViradasDiagonalDescendoDireita(jogador, outroJogador, linha, coluna)
        if(retornoDescendoDireita != None):
            try:
                if(len(retornoDescendoDireita["pecasViradas"]) > 0):
                    resultadoJogada[retornoDescendoDireita["posicao"]] += retornoDescendoDireita["pecasViradas"]
            except:
                resultadoJogada[retornoDescendoDireita["posicao"]] = retornoDescendoDireita["pecasViradas"]


    def pegaPecasViradasDiagonalSubindoEsquerda(self, jogador, outroJogador, linha, coluna):
        if((coluna <= 0) or (linha <= 0) or self.tabuleiro[linha-1][coluna-1] == jogador):
            return None
        
        if(self.tabuleiro[linha-1][coluna-1] == outroJogador):
            resultadoJogada = self.pegaPecasViradasDiagonalSubindoEsquerda(jogador, outroJogador, linha - 1, coluna - 1)
            if(resultadoJogada != None):
                resultadoJogada["pecasViradas"].append((linha - 1, coluna - 1))
            return resultadoJogada
        
        elif(self.tabuleiro[linha-1][coluna-1] == "-"):
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
        
        elif(self.tabuleiro[linha+1][coluna+1] == "-"):
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
        
        elif(self.tabuleiro[linha-1][coluna+1] == "-"):
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
        
        elif(self.tabuleiro[linha+1][coluna-1] == "-"):
            return {"posicao": (linha+1, coluna-1), "pecasViradas": []}

        return None


    def __str__(self):
        saida = "   "

        for i in range(len(self.tabuleiro)):
            saida += str(i) + "  "

        saida += "\n"

        for i in range(len(self.tabuleiro)):
            saida += str(i) + "  "
            
            for j in range(len(self.tabuleiro)):
                saida += str(self.tabuleiro[i][j]) + "  "
            
            saida += "\n"

        return saida
    

    def exportar(self):
        dicionarioTabuleiro = {}
        for i in range(len(self.tabuleiro)):
            dicionarioTabuleiro[str(i)] = {}
            for j in range(len(self.tabuleiro)):
                dicionarioTabuleiro[str(i)][str(j)] = self.tabuleiro[i][j]

        print(dicionarioTabuleiro)
        dicionario = {
            "tamanho" : self.tamanho,
            "tabuleiro" : dicionarioTabuleiro,
            "pontuacao" : self.pontuacao,

        }
        return dicionario