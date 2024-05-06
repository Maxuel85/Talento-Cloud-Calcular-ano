import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.date.today().year
    idade = ano_atual - ano_nascimento
    return idade

def main():
    while True:
        nome_completo = input("Digite seu nome completo: ")
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                break
            else:
                print("Por favor, digite um ano entre 1922 e 2021.")
        except ValueError:
            print("Por favor, digite um ano válido.")

    idade = calcular_idade(ano_nascimento)
    print(f"Olá, {nome_completo}! Você completou ou completará {idade} anos em 2022.")

if __name__ == "__main__":
    main()