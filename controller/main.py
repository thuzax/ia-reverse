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

    resultadoIA = None
    jogoTerminou = True if (tabuleiro.pontuacao["B"] + tabuleiro.pontuacao["P"] == 64) else False
    if(resultadoJogada and not jogoTerminou):
        outroJogador = "P" if args["jogador"] == "B" else "B"
        arvore = Arvore(outroJogador, 4)
        arvore.adicionaNoh(tabuleiro)
        jogada = arvore.preveJogada()
        if(jogada != None):
            resultadoIA = jogada.exporta()
        else:
            resultadoIA = resultado
        
        resultadoIA["jogadaFeita"] = True
        
        # print(arvore)
    resultadoFinal = {}
    resultadoFinal["jogador"] = resultado
    if(resultadoIA != None):
        resultadoFinal["ia"] = resultadoIA
    else:
        resultadoFinal["ia"] = resultado
    
    return (json.dumps(resultadoFinal))