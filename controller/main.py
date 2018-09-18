from Tabuleiro import Tabuleiro


def main():
    tabuleiro = Tabuleiro(8)
    i = 0
    j = 0
    cont = 0
    while(cont < tabuleiro.tamanho**2):
        print(tabuleiro)
        print(tabuleiro.pontuacao)
        jogador = "B"
        if(cont % 2 == 0):
            jogador = "P"
            
        posicoes = input().split(" ")
        jogadaFeita = tabuleiro.fazerJogada(jogador, int(posicoes[0]), int(posicoes[1]))
        if(jogadaFeita):
            cont += 1
        else:
            print("Jogada invalida! Escolha outra posicao")

    print(tabuleiro)
    print(tabuleiro.pontuacao)


main()