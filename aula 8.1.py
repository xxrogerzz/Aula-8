print("=== Bem-vindo ao Sistema de Reservas de Hotel ===")

# Listas de tipos de quartos e preços
quartos = ["Simples", "Duplo", "Luxo"]
precos = [100.00, 150.00, 250.00]

# Lista para armazenar clientes
clientes = []

# Cadastro de até 3 clientes usando 'for'
for i in range(1, 4):
    print(f"\nCadastro do Cliente {i}")
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    if idade < 18:
        print("Clientes menores de 18 anos não podem fazer reserva.")
        continue

    print("\nTipos de quarto disponíveis:")
    for j, quarto in enumerate(quartos, start=1):
        print(f"{j} - {quarto} (R$ {precos[j-1]:.2f}/dia)")

    escolha_quarto = int(input("Escolha o tipo de quarto (1, 2 ou 3): "))

    if escolha_quarto in range(1, 4):
        tipo_quarto = quartos[escolha_quarto - 1]
        preco_diaria = precos[escolha_quarto - 1]
    else:
        print("Opção inválida. Reserva cancelada para esse cliente.")
        continue

    dias = int(input("Quantos dias ficará hospedado? "))

    if dias <= 0:
        print("Número de dias inválido. Reserva cancelada para esse cliente.")