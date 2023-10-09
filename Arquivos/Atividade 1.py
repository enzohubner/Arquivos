estudantes = []

conf = "sim"

while conf == "sim":
    nome = input("Digite o nome do estudante: ")
    idade = input("Digite a idade: ")
    curso = input("Digite o curso: ")
    
    estudante = {"Nome": nome, "Idade": idade, "Curso": curso}
    
    estudantes.append(estudante)

    conf = input("Deseja continuar? ")

with open("estudante.txt", "w") as arquivo:
    for estudante in estudantes:
        arquivo.write("Estudante:\n")
        for chave, valor in estudante.items():
            arquivo.write(f"{chave}: {valor}\n")
        arquivo.write("\n")