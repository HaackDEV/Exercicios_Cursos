def consumo_combustivel(distancia, valor, litros):   # Função para calcular o consumo de combustível

        if litros == 0:   # Verifica se a quantidade de combustível consumido é zero
                print("A quantidade de combustível consumido não pode ser zero.")
                print("Por favor, tente novamente.")
                return   # Volta para o início do programa
        
        consumo_medio = distancia / litros   # Cálculo do consumo médio de combustível
        
        print(f"\nA distância percorrida foi de {distancia:.2f} km.")
        print(f"O valor do combustível foi de R$ {valor:.2f}.")
        print(f"A quantidade de combustível consumido foi de {litros:.2f} litros.")

        done = str(input("\nDigite Y para calcular o consumo médio de combustível ou N para sair do programa: ")).strip().upper() # Verifica se o usuário quer continuar ou sair do programa
        if done == "Y":
                print("\nCalculando...")
                print(f"O consumo médio de combustível foi de {consumo_medio:.2f} km/l.")
                return True   #Continua o programa
        else:
                print("Saindo do programa.")
                return False   # Sai do programa

print("\nSeja bem-vindo ao programa de consumo de combustível!")
print("Este programa calcula o consumo de combustível de um veículo.")

while True:

    try:       
        distancia = float(input("\nDigite a distância percorrida (em km): "))
        valor = float(input("Digite o valor do combustível (em R$): "))
        litros = float(input("Digite a quantidade de combustível consumido (em litros): "))
        continuar = consumo_combustivel(distancia, valor, litros)   # Chama a função para calcular o consumo de combustível
        if continuar is False:
            break 
    except ValueError:
        print("\nErro: Por favor, insira números válidos.")