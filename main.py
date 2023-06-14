import random
main = True
resultado = [3,16,23,41,45,57]

def gerar_combinacao_mega_sena():
    numeros = random.sample(range(1, 61), 6)
    numeros.sort()
    return numeros

def main():
    combinacao = gerar_combinacao_mega_sena()
    print("Sua combinação de números da Mega-Sena é:")
    print(combinacao)

if __name__ == '__main__':
    main()

while main() != resultado:
    if main() == resultado:
        main()
