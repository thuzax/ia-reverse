from Tabuleiro import Tabuleiro
from Arvore import Arvore
import json
import sys


def main(args):
    tabuleiro = Tabuleiro(8)
    tabuleiro.lerTabuleiro(args["tabuleiro"])
    resultadoJogada = tabuleiro.fazJogada(args["jogador"], int(args["posicaoI"]), int(args["posicaoJ"]))
    resultado = tabuleiro.exporta()
    resultado["jogadaFeita"] = resultadoJogada

    if(resultadoJogada):
        outroJogador = "P" if args["jogador"] == "B" else "B"
        arvore = Arvore(outroJogador, 2)
        arvore.adicionaNoh(tabuleiro)
        jogada = arvore.preveJogada()
        print(arvore)

    return (json.dumps(resultado))