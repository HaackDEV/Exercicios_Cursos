 #Sistema simples de uma lanchonete

produtosA = {
    1: {"nome": "Xis salada", "preco": 25.00},
    2: {"nome": "Xis frango", "preco": 25.00},
    3: {"nome": "Xis bacon", "preco": 30.00},
    4: {"nome": "Xis filé", "preco": 33.00},
    5: {"nome": "Xis tudo", "preco":36.00},
    6: {"nome": "Refrigerante Lata", "preco": 8.50},
    7: {"nome": "Suco", "preco": 8.00},
    8: {"nome": "Água", "preco": 5.00},
    9: {"nome": "Cerveja", "preco": 12.00},
    10: {"nome": "Drink", "preco": 25.00},
}

print("Bem-vindo ao sistema do XIS KING!")
print("Vamos fechar o seu pedido!")

try:
    while True:
        codigo = int (input("Digite o codigo do produto: "))
        quantidade = int (input("Digite a quantidade do produto: "))
        if quantidade < 1:
            print("Erro: A quantidade deve ser maior que 0.")
            continue
        else:
            break

    fechamento_pedido = []

    while True:

        if codigo in produtosA:
            valorProduto = produtosA[codigo]["preco"]
            valorTotal = valorProduto * quantidade
            fechamento_pedido.append((produtosA[codigo]["nome"], quantidade, valorTotal))
            print(f"Produto: {produtosA[codigo]['nome']}, Quantidade: {quantidade}, Valor Total: R$ {valorTotal:.2f}")
        else:
            print("Código inválido. Tente novamente.")
        
        continuar = input("Deseja adicionar mais produtos? (S/N): ").strip().upper()
        if continuar == "N":
            print("\nResumo do pedido:")
            total_geral = 0
            for nome_produto, quantidade, valorTotal in fechamento_pedido:
                unidade = "unidade" if quantidade == 1 else "unidades"
                print(f"{nome_produto} - {quantidade} {unidade} - R$ {valorTotal:.2f}")
                total_geral += valorTotal
            print(f"\nTotal a pagar: R$ {total_geral:.2f}")
            break
        elif continuar != "S":
            print("Opção inválida. Tente novamente.")
            continue
        
        codigo = int(input("Digite o código do produto: "))
        quantidade = int(input("Digite a quantidade do produto: ")) 

except ValueError:
    print("Erro: Por favor, insira números válidos.")
    