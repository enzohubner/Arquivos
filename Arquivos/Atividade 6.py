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

idades = [int(estudante.get("Idade", "0")) for estudante in estudantes]
total_idades = sum(idades)
numero_estudantes = len(estudantes)

if numero_estudantes > 0:
    idade_media = total_idades / numero_estudantes
else:
    idade_media = 0

print(f"A idade média dos {numero_estudantes} estudantes é de {idade_media:.2f} anos.")