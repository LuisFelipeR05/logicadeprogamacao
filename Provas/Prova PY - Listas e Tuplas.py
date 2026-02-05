# Cadastro de 5 alunos em uma lista de tuplas
alunos = []

for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    alunos.append((nome, nota))

# Encontrar o aluno com a maior nota
aluno_maior_nota = max(alunos, key=lambda x: x[1])

print(f"O aluno com a maior nota é: {aluno_maior_nota[0]} (nota {aluno_maior_nota[1]})")
