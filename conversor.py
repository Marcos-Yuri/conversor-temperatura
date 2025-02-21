def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    while True:
        print("\nConversor de Temperatura")
        print("1. Celsius para Fahrenheit")
        print("2. Fahrenheit para Celsius")
        print("3. Sair")

        escolha = input("Escolha a opção (1, 2 ou 3): ")

        if escolha == '1':
            try:
                celsius = float(input("Digite a temperatura em Celsius: "))
                print(f"{celsius}°C = {celsius_para_fahrenheit(celsius):.2f}°F")
            except ValueError:
                print("Erro: Insira um número válido.")
        elif escolha == '2':
            try:
                fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
                print(f"{fahrenheit}°F = {fahrenheit_para_celsius(fahrenheit):.2f}°C")
            except ValueError:
                print("Erro: Insira um número válido.")
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")
