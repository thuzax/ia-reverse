from Noh import Noh
from Tabuleiro import Tabuleiro
from MatrizPesos import MatrizPesos

class Arvore:
    def __init__(self, jogador, nivel, matrizPesos):
        self.raiz = None
        self.jogador = jogador
        self.oponente = "B" if self.jogador == "P" else "P"
        self.nivel = nivel
        self.matrizPesos = matrizPesos
        self.folhas = []

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
            if(len(jogadasOrdenadas) < 6):
                jogadasOrdenadas.append({posicoes: resultadoPontos})
            return


    def escolheMelhoresJogadas(self, jogador, oponente, atual, jogadas):
        jogadasOrdenadas = []
        for posicoes in jogadas:
            pesoPosicao = self.matrizPesos.getPeso(posicoes[0], posicoes[1])
            novaPontuacaoJogador = atual.tabuleiro.pontuacao[jogador] + len(jogadas[posicoes]) + pesoPosicao
            novaPontuacaoOponente = atual.tabuleiro.pontuacao[oponente] - len(jogadas[posicoes])
            resultadoPontos = novaPontuacaoJogador - novaPontuacaoOponente
            self.insereOrdenado(posicoes, jogadasOrdenadas, resultadoPontos)

        melhoresJogadas = {}
        for dicionario in jogadasOrdenadas:
            chave = list(dicionario.keys())[0]
            melhoresJogadas[chave] = jogadas[chave]
        return melhoresJogadas

    def escolheMelhorFolha(self):
        if(len(self.folhas) == 0):
            return self.raiz
        
        melhor = self.folhas[0]
        for i in range(1, len(self.folhas)):
            if(melhor.ganho < self.folhas[i].ganho):
                melhor = self.folhas[i]
        return melhor
        


    def encontraInicioDaJogada(self, noh):
        if(noh.pai == None):
            return noh
        if(noh.pai.pai == None):
            return noh
        return self.encontraInicioDaJogada(noh.pai)
        

    def preveJogada(self):
        self.geraArvoreDePossibilidades(self.raiz, 0)
        melhorFolha = self.escolheMelhorFolha()
        jogada = self.encontraInicioDaJogada(melhorFolha)
        return jogada.tabuleiro



    def geraArvoreDePossibilidades(self, atual, iteracao):
        if(iteracao == self.nivel):
            self.folhas.append(atual)
            return
        
        jogadorAtual = self.jogador
        oponenteAtual = self.oponente
        if(iteracao % 2 != 0):
            jogadorAtual = self.oponente
            oponenteAtual = self.jogador
        
        jogadas = atual.tabuleiro.pegaJogadasPossiveis(jogadorAtual, oponenteAtual)
        melhoresJogadas = self.escolheMelhoresJogadas(jogadorAtual, oponenteAtual, atual, jogadas)
        #por aqui
        if(len(jogadas) == 0):
            novoTabuleiro = atual.tabuleiro.copy()
            self.adicionaNoh(novoTabuleiro, atual)
        else:
            for jogada in melhoresJogadas:
                novoTabuleiro = atual.tabuleiro.copy()
                novoTabuleiro.fazJogada(jogadorAtual, jogada[0], jogada[1])
                self.adicionaNoh(novoTabuleiro, atual)
        
        for filho in atual.filhos:
            self.geraArvoreDePossibilidades(filho, iteracao + 1)


        # jogada = self.escolheJogada(jogadorAtual, oponenteAtual, atual)
            


    def __str__(self):
        return self.retornaArvore(self.raiz, "", 0, 0)

    def retornaArvore(self, noh, saida, nivel, identificador):
        saida += "====== Nivel: " + str(nivel) + " ID: " + str(identificador) + " ==================\n"
        saida += str(noh.tabuleiro)
        
        for i in range(len(noh.filhos)):
            saida = self.retornaArvore(noh.filhos[i], saida, nivel + 1, i)
        
        return saida
