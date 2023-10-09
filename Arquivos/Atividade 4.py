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

nome_pesquisa = input("Digite o nome do estudante que deseja procurar: ")

estudantes_encontrados = []

for estudante in estudantes:
    if estudante.get("Nome", "").lower() == nome_pesquisa.lower():
        estudantes_encontrados.append(estudante)

if estudantes_encontrados:
    for i, estudante in enumerate(estudantes_encontrados, start=1):
        print(f"Informações do Estudante {i}:")
        for chave, valor in estudante.items():
            print(f"{chave}: {valor}")
        print()