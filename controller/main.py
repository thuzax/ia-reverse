from Tabuleiro import Tabuleiro


def main():
    tabuleiro = Tabuleiro(6)
    # print(tabuleiro)
    print(tabuleiro)
    i = 0
    j = 0
    cont = 0
    while(i != -1 and j != -1):
        tabuleiro.jogadaPossivel(None, None, None)
        print(tabuleiro.pontuacao)
        i = int(input())
        j = int(input())
        jogador = "P"
        if(cont % 2 == 1):
            jogador = "B"
        tabuleiro.fazerJogada(jogador, i, j)
        print(tabuleiro)
        cont += 1


main()