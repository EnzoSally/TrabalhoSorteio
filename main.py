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

aposta = []

while len(aposta) < 6:
    dezena = int(input('Digite uma dezena da aposta: '))
    if dezena not in aposta and dezena < 60:
        aposta.append(dezena)
    elif dezena > 60:
        print("O número deve ser menor do que 60")
    else:
        print("Número já foi colocado, por favor escolha outro.")


if __name__ == '__main__':
    main()


    

