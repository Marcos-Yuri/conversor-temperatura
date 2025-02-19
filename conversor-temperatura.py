def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Conversor de Temperatura")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    
    escolha = input("Escolha a opção (1 ou 2): ")

    if escolha == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"{celsius}°C = {celsius_para_fahrenheit(celsius):.2f}°F")
    elif escolha == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"{fahrenheit}°F = {fahrenheit_para_celsius(fahrenheit):.2f}°C")
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
