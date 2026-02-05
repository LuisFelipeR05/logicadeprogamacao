def calcular_medias(alunos):

    medias = {}
    for nome, notas in alunos.items():
        if notas:  # evita divisão por zero
            medias[nome] = sum(notas) / len(notas)
        else:
            medias[nome] = 0.0
    return medias

def mostrar_aprovados(medias, limite=7.0):

    aprovados = {nome: media for nome, media in medias.items() if media >= limite}
    if aprovados:
        print("Aprovados (média >= {:.1f}):".format(limite))
        for nome, media in aprovados.items():
            print(f"- {nome}: {media:.2f}")
    else:
        print("Nenhum aluno aprovado com média >= {:.1f}.".format(limite))


if __name__ == "__main__":

    alunos = {
        "Ana": [8.5, 7.0, 9.0],
        "Bruno": [6.0, 5.5, 6.5],
        "Carla": [7.0, 7.0, 7.0],
        "Diego": [9.0, 8.5, 10.0],
        "Luis" : [9.2, 9.5, 9.8],
    }

    medias = calcular_medias(alunos)
    print("Médias dos alunos:")
    for nome, media in medias.items():
        print(f"{nome}: {media:.2f}")

    print()  
    mostrar_aprovados(medias, limite=7.0)
