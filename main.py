class Deque:
    class __No:
        def __init__(self, dado=None):
            self.dado = dado
            self.proximo = None
            self.anterior = None

    def __init__(self):
        self.__cabeca = self.__No()
        self.__cauda = self.__No()
        self.__cabeca.proximo = self.__cauda
        self.__cauda.anterior = self.__cabeca
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def getSize(self):
        return self.__size

    def peek(self):
        if self.is_empty():
            return None
        return self.__cabeca.proximo.dado

    def top(self):
        if self.is_empty():
            return None
        return self.__cauda.anterior.dado

    def __str__(self):
        elementos = []
        atual = self.__cabeca.proximo
        while atual != self.__cauda:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        return " ".join(elementos)

    def addFirst(self, dado):
        novo_no = self.__No(dado)
        primeiro = self.__cabeca.proximo
        novo_no.proximo = primeiro
        novo_no.anterior = self.__cabeca
        primeiro.anterior = novo_no
        self.__cabeca.proximo = novo_no
        self.__size += 1

    def addLast(self, dado):
        novo_no = self.__No(dado)
        ultimo = self.__cauda.anterior
        novo_no.proximo = self.__cauda
        novo_no.anterior = ultimo
        ultimo.proximo = novo_no
        self.__cauda.anterior = novo_no
        self.__size += 1

    def deleteFirst(self):
        if self.is_empty():
            print("Deque vazio")
            return None
        removido = self.__cabeca.proximo
        self.__cabeca.proximo = removido.proximo
        removido.proximo.anterior = self.__cabeca
        self.__size -= 1
        return removido.dado

    def deleteLast(self):
        if self.is_empty():
            print("Deque vazio")
            return None
        removido = self.__cauda.anterior
        self.__cauda.anterior = removido.anterior
        removido.anterior.proximo = self.__cauda
        self.__size -= 1
        return removido.dado

    def inserir_posicao(self, dado, posicao):
        if posicao < 0 or posicao > self.__size:
            print("Posição inválida.")
            return
        atual = self.__cabeca.proximo
        for _ in range(posicao):
            atual = atual.proximo
        novo_no = self.__No(dado)
        novo_no.proximo = atual
        novo_no.anterior = atual.anterior
        atual.anterior.proximo = novo_no
        atual.anterior = novo_no
        self.__size += 1

    def remover_posicao(self, posicao):
        if posicao < 0 or posicao >= self.__size:
            print("Posição inválida.")
            return None
        atual = self.__cabeca.proximo
        for _ in range(posicao):
            atual = atual.proximo
        removido = atual
        removido.anterior.proximo = removido.proximo
        removido.proximo.anterior = removido.anterior
        self.__size -= 1
        return removido.dado

    def remover_dado(self, dado):
        atual = self.__cabeca.proximo
        for _ in range(self.__size):
            if atual.dado == dado:
                atual.anterior.proximo = atual.proximo
                atual.proximo.anterior = atual.anterior
                self.__size -= 1
                return atual.dado
            atual = atual.proximo
        print("Dado não encontrado.")
        return None

    def recuperar_posicao(self, posicao):
        if posicao < 0 or posicao >= self.__size:
            print("Posição inválida.")
            return None
        atual = self.__cabeca.proximo
        for _ in range(posicao):
            atual = atual.proximo
        return atual.dado

    def imprimir_lista(self):
        atual = self.__cabeca.proximo
        for _ in range(self.__size):
            print(atual.dado, end=" <-> ")
            atual = atual.proximo
        print("None")

    def obter_cabeca(self):
        return self.__cabeca

    def obter_cauda(self):
        return self.__cauda


# Testando o Deque
deque = Deque()

# Inserindo e exibindo elementos no início.
print("Inserindo 10 no início do deque:")
deque.addFirst(10)
print(deque)  # Deve imprimir: 10.

print("Inserindo 5 no início do deque:")
deque.addFirst(5)
print(deque)  # Deve imprimir: 5 10.

# Inserindo e exibindo elementos no final.
print("Inserindo 20 no final do deque:")
deque.addLast(20)
print(deque)  # Deve imprimir: 5 10 20.

print("Inserindo 30 no final do deque:")
deque.addLast(30)
print(deque)  # Deve imprimir: 5 10 20 30.

# Removendo e exibindo elemento do início.
print("\nRemovendo elemento do início do deque:")
deque.deleteFirst()
print(deque)  # Deve imprimir: 10 20 30.

print("Removendo outro elemento do início do deque:")
deque.deleteFirst()
print(deque)  # Deve imprimir: 20 30.

# Removendo e exibindo elemento do final.
print("Removendo elemento do final do deque:")
deque.deleteLast()
print(deque)  # Deve imprimir: 20.

print("Removendo outro elemento do final do deque:")
deque.deleteLast()
print(deque)  # Deve imprimir: None.

# Verificando se o deque está vazio e tentando remover de um deque vazio.
print("\nO deque está vazio?", deque.is_empty())  # Deve imprimir: True.
print("Tentando remover de um deque vazio:")
deque.deleteFirst()  # Deve imprimir mensagem de erro.
