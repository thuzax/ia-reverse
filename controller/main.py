from Tabuleiro import Tabuleiro
import json
import sys


def main(args):
    tabuleiro = Tabuleiro(8)
    print("\n++++++++++\n+++++++++++++\n")
    # trem = args[0].decode("utf-8")
    # print(trem)
    print(args)
    tabuleiro.lerTabuleiro(args["tabuleiro"])
    resultadoJogada = tabuleiro.fazerJogada(args["jogador"], int(args["posicaoI"]), int(args["posicaoJ"]))
    print("----------------------------------------")
    print(tabuleiro)
    resultado = tabuleiro.exportar()
    resultado["jogadaFeita"] = resultadoJogada
    return (json.dumps(resultado))