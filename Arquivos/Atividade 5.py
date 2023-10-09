estudantes = []

with open("estudantes.txt", "r") as arquivo:
    estudante_atual = {}

    for linha in arquivo:
        linha = linha.strip()

        if linha.startswith("Estudante:"):
            if estudante_atual:
                estudantes.append(estudante_atual)
            estudante_atual = {}
        else:
            chave, valor = linha.split(": ")
            estudante_atual[chave] = valor

if estudante_atual:
    estudantes.append(estudante_atual)

for i, estudante in enumerate(estudantes, start=1):
    print(f"Estudante {i}:")
    for chave, valor in estudante.items():
        print(f"{chave}: {valor}")
    print()

nome_remover = input("Digite o nome do estudante que deseja remover: ")

estudantes_modificados = []
removido = False

for estudante in estudantes:
    if estudante.get("Nome", "").lower() != nome_remover.lower():
        estudantes_modificados.append(estudante)
    else:
        removido = True

with open("estudantes.txt", "w") as arquivo:
    for estudante in estudantes_modificados:
        arquivo.write("Estudante:\n")
        for chave, valor in estudante.items():
            arquivo.write(f"{chave}: {valor}\n")
        arquivo.write("\n")