class MatrizPesos:

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.matrizPesos = []
        for i in range(self.tamanho):
            self.matrizPesos.append([])
            for j in range(self.tamanho):
                self.matrizPesos[i].append(1)

        for i in range(self.tamanho):
            self.matrizPesos[i][0] = 8
            self.matrizPesos[0][i] = 8
            self.matrizPesos[i][self.tamanho - 1] = 8
            self.matrizPesos[self.tamanho - 1][i] = 8
            
        for i in range(self.tamanho):
            self.matrizPesos[i][1] = -8
            self.matrizPesos[i][self.tamanho - 2] = -8
            self.matrizPesos[1][i] = -8
            self.matrizPesos[self.tamanho - 2][i] = -8
        


        self.matrizPesos[0][0] += 8
        self.matrizPesos[0][self.tamanho - 1] += 8
        self.matrizPesos[self.tamanho - 1][0] += 8
        self.matrizPesos[self.tamanho - 1][self.tamanho - 1] += 8
        
        self.matrizPesos[1][1] = -7
        self.matrizPesos[1][self.tamanho - 2] = -7
        self.matrizPesos[self.tamanho - 2][1] = -7
        self.matrizPesos[self.tamanho - 2][self.tamanho - 2] = -7

    def getPeso(self, linha, coluna):
        return self.matrizPesos[linha][coluna]