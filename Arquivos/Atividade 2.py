with open("estudantes.txt", "r") as arquivo:
    estudante_atual = {}  # Dicionário temporário para armazenar os detalhes do estudante atual

    for linha in arquivo:
        linha = linha.strip()

        if linha.startswith("Estudante:"):
            if estudante_atual:
                estudantes.append(estudante_atual)
            estudante_atual = {}  # Inicie um novo dicionário para o próximo estudante
        else:
            chave, valor = linha.split(": ")
            estudante_atual[chave] = valor

# Certifique-se de adicionar o último estudante à lista
if estudante_atual:
    estudantes.append(estudante_atual)

# Imprima as informações dos estudantes na tela
for i, estudante in enumerate(estudantes, start=1):
    print(f"Estudante {i}:")
    for chave, valor in estudante.items():
        print(f"{chave}: {valor}")
    print()