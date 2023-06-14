import random

def gerar_combinacao_mega_sena():
    numeros = random.sample(range(1, 61), 6)
    numeros.sort()
    return numeros

def contador():
    contador = 0
    maximo_sorteios = 10
    while contador > maximo_sorteios:
        contador += 1
        sorteio = gerar_combinacao_mega_sena()
        print(f"Sorteio {contador}: {sorteio}")

def main():
    combinacao = gerar_combinacao_mega_sena()
    print("Sua combinação de números da Mega-Sena é:")
    print(combinacao)

if __name__ == '__main__':
    main()


    

