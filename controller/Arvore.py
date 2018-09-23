from Noh import Noh
from Tabuleiro import Tabuleiro
class Arvore:
    def __init__(self, jogador, nivel):
        self.raiz = None
        self.jogador = jogador
        self.oponente = "B" if self.jogador == "P" else "P"
        self.nivel = nivel

    def adicionaNoh(self, tabuleiro, pai = None):
        novo = Noh(tabuleiro)
        if(self.raiz == None):
            self.raiz = novo
            return
        novo.ganho = tabuleiro.pontuacao[self.jogador] - tabuleiro.pontuacao[self.oponente]
        novo.pai = pai
        pai.filhos.append(novo)

    def insereNaPosicao(self, jogadasOrdenadas, posicoes, resultadoPontos):
        for i in range(len(jogadasOrdenadas)):
            pontuacaoJogada = list(jogadasOrdenadas[i].items())[0]
            if(pontuacaoJogada < resultadoPontos):
                jogadasOrdenadas.insert(i, {posicoes: resultadoPontos})
                return True
        
        return False

    def insereOrdenado(self, posicoes, jogadasOrdenadas, resultadoPontos):
        if(len(jogadasOrdenadas) == 0):
            jogadasOrdenadas.append({posicoes: resultadoPontos})
            return
        
        melhorPontuacao = list(jogadasOrdenadas[0].values())[0]
        if(resultadoPontos > melhorPontuacao - 2):
            inserido = self.insereNaPosicao(jogadasOrdenadas, posicoes, resultadoPontos)
            if(inserido):
                return
            if(len(jogadasOrdenadas) < 8):
                jogadasOrdenadas.append({posicoes: resultadoPontos})
            return



    def escolheMelhoresJogadas(self, jogador, oponente, atual, jogadas):
        jogadasOrdenadas = []
        for posicoes in jogadas:
            novaPontuacaoJogador = atual.tabuleiro.pontuacao[jogador] + len(jogadas[posicoes]) + 1
            novaPontuacaoOponente = atual.tabuleiro.pontuacao[oponente] - len(jogadas[posicoes])
            resultadoPontos = novaPontuacaoJogador - novaPontuacaoOponente
            self.insereOrdenado(posicoes, jogadasOrdenadas, resultadoPontos)

        melhoresJogadas = {}
        for dicionario in jogadasOrdenadas:
            chave = list(dicionario.keys())[0]
            melhoresJogadas[chave] = jogadas[chave]
        return melhoresJogadas

    def escolheMelhorFolha(self, noh):
        if(len(noh.filhos) == 0):
            return noh

        melhor = None
        for filho in noh.filhos:
            melhorFilho = self.escolheMelhorFolha(filho)
            if(melhor == None):
                melhor = melhorFilho
            elif(melhor.ganho < melhorFilho.ganho):
                melhor = melhorFilho
        return melhor
        


    def encontraInicioDaJogada(self, noh):
        if(noh.pai == None):
            return None
        if(noh.pai.pai == None):
            return noh
        
        return self.encontraInicioDaJogada(noh.pai)
        

    def preveJogada(self):
        self.geraArvoreDePossibilidades(self.raiz, 0)
        melhorFolha = self.escolheMelhorFolha(self.raiz)
        return self.encontraInicioDaJogada(melhorFolha).tabuleiro



    def geraArvoreDePossibilidades(self, atual, iteracao):
        if(iteracao == self.nivel):
            return
        
        jogadorAtual = self.jogador
        oponenteAtual = self.oponente
        if(iteracao % 2 != 0):
            jogadorAtual = self.oponente
            oponenteAtual = self.jogador
        
        jogadas = atual.tabuleiro.pegaJogadasPossiveis(jogadorAtual, oponenteAtual)
        melhoresJogadas = self.escolheMelhoresJogadas(jogadorAtual, oponenteAtual, atual, jogadas)
        for jogada in melhoresJogadas:
            novoTabuleiro = atual.tabuleiro.copy()
            novoTabuleiro.fazJogada(jogadorAtual, jogada[0], jogada[1])
            self.adicionaNoh(novoTabuleiro, atual)

        for filho in atual.filhos:
            resultado = self.geraArvoreDePossibilidades(filho, iteracao + 1)


        # jogada = self.escolheJogada(jogadorAtual, oponenteAtual, atual)
            



    def __str__(self):
        return self.retornaArvore(self.raiz, "", 0, 0)

    def retornaArvore(self, noh, saida, nivel, identificador):
        saida += "====== Nivel: " + str(nivel) + " ID: " + str(identificador) + " ==================\n"
        saida += str(noh.tabuleiro)
        
        for i in range(len(noh.filhos)):
            saida = self.retornaArvore(noh.filhos[i], saida, nivel + 1, i)
        
        return saida
