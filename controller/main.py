from Tabuleiro import Tabuleiro
import json
import sys


def main(args):
    tabuleiro = Tabuleiro(8)
    print("\n++++++++++\n+++++++++++++\n")
    # trem = args[0].decode("utf-8")
    # print(trem)
    tabuleiro.lerTabuleiro(args["tabuleiro"])
    print(tabuleiro)
    # i = 0
    # j = 0
    # cont = 0
    # while(cont < tabuleiro.tamanho**2):
    #     print(tabuleiro)
    #     print(tabuleiro.pontuacao)
    #     jogador = "B"
    #     if(cont % 2 == 0):
    #         jogador = "P"
            
    #     posicoes = input().split(" ")
    #     jogadaFeita = tabuleiro.fazerJogada(jogador, int(posicoes[0]), int(posicoes[1]))
    #     if(jogadaFeita):
    #         cont += 1
    #     else:
    #         print("Jogada invalida! Escolha outra posicao")

    # print(tabuleiro)
    # print(tabuleiro.pontuacao)

    
    # print(tabuleiro.exportar())
    return (tabuleiro.exportar())