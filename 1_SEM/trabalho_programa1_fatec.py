aprovado = 0 #contagem de aprovados na faculdade
reprovado = 0 #contagem de reprovados na faculdade
disciplina = 0 #contador das quantidade de disciplinas, curso 1
total_disciplinas = 0 #soma de todas as médias das disciplinas
total_alunos = 0 #soma de todos os alunos de um curso

disciplina_2 = 0 #contador das quantidade de disciplinas, curso 2
resultado_disciplina2 = 0 #resultado disciplina
total_alunos_2 = 0 #total de alunos no curso 2
total_disciplinas_2 = 0 #soma de todas as médias das disciplinas do curso 2



print("Bem-Vindo ao software da faculdade Tecfa")
print("-------------")
print("Esse sofware o ajudará gerenciar o cursos, alunos, notas e se foram aprovados, reprovados")
print("-------------")
curso_1 = int(input("Digite 1 se o curso for [Segurança da Informação] ou Digite 2 para [Desenvolvimento de Sistemas]: "))
if curso_1 == 1:
    print("Curso selecionado foi [Segurança da Informação]")
else:
    print("Curso selecionado foi [Desenvolvimento de Sistemas]")
quantidade_diciplina = int(input("Quantas diciplinas tem o curso? "))

#curso 1
while disciplina < quantidade_diciplina: #laço das contagem de diciplina
    print("-------------------------------")
    print("disciplina", disciplina + 1)
    print("-------------------------------")
    alunos = 0 #contador de alunos
    soma_media = 0 #Soma das médias dos alunos 
    numero_alunos = int(input("Quantos alunos tem sua disciplina? "))
    print("-------------")
    while alunos < numero_alunos: #Laço contagem de alunos
        nome = input("Informe o nome do aluno: ")
        p1 = int(input("Digite a 1ª nota: "))
        p2 = int(input("Digite a 2ª nota: "))
        media = (p1 + p2) / 2
        if media >= 6:
            print("-------------")
            print("A média do aluno", nome, "é", media,"(Aprovado)")
            print("-------------")
            aprovado = aprovado + 1
        else:
            print("-------------")
            print("A média do aluno", nome, "é", media,"(Reprovado)")
            print("-------------")
            reprovado = reprovado + 1
        soma_media = soma_media + media
        alunos = alunos + 1 #contador
    disciplina_media = soma_media / numero_alunos
    print("Média da disciplina", disciplina + 1,":", disciplina_media)
    total_disciplinas = total_disciplinas + disciplina_media #soma de todas as médias das disciplinas
    total_alunos = total_alunos + alunos #soma de todos os alunos de um curso
    disciplina = disciplina + 1 #contador
print("-----------------------")
print("Media do curso 1 feita com sucesso.")
auxiliar_aprovado_1 = aprovado
auxiliar_reprovado_1 = reprovado
#Média da curso 1
media_curso1 = total_disciplinas / quantidade_diciplina
print("Media Total do curso 1:", media_curso1)
print("Total de alunos no curso 1:", total_alunos)
print("Total de Aprovados:", aprovado)
print("Total de Reprovados:", reprovado)
print("-----------------------")

curso_2 = int(input("Digte 2 para proseguir para o proximo curso: "))
if curso_2 == 2:
    quantidade_diciplina_2 = int(input("Quantas diciplinas tem o curso? "))
    #curso 2
    aprovado = 0
    reprovado = 0
    while disciplina_2 < quantidade_diciplina_2: #laço das contagem de diciplina
        print("-------------------------------")
        print("disciplina", disciplina_2 + 1)
        print("-------------------------------")
        alunos = 0 #contador de alunos
        soma_media_2 = 0 #Soma das médias dos alunos 
        numero_alunos_2 = int(input("Quantos alunos tem sua disiplina(s)? "))
        print("-------------")
        while alunos < numero_alunos_2: #laço inicial, contagem de alunos
            nome = input("Informe o nome do aluno: ")
            p1 = int(input("Digite a 1ª nota: "))
            p2 = int(input("Digite a 2ª nota: "))
            media_2 = (p1 + p2) / 2
            if media_2 >= 6:
                print("-------------")
                print("A média do aluno", nome, "é", media_2,"(Aprovado)")
                print("-------------")
                aprovado = aprovado + 1
            else:
                print("-------------")
                print("A média do aluno", nome, "é", media_2,"(Reprovado)")
                print("-------------")
                reprovado = reprovado + 1
            soma_media_2 = soma_media_2 + media_2
            alunos = alunos + 1 #contador
        disciplina_media_2 = soma_media_2 / numero_alunos_2
        print("Média da disciplina", disciplina_2 + 1,":", disciplina_media_2)
        total_disciplinas_2 = total_disciplinas_2 + disciplina_media_2 #soma de todas as médias das disciplinas
        total_alunos_2 = total_alunos_2 + alunos #soma de todos os alunos de um curso
        disciplina_2 = disciplina_2 + 1 #contador
    print("-----------------------")
    print("Média do curso 2 feitas com sucesso.")
    auxiliar_aprovado_2 = aprovado
    auxiliar_reprovado_2 = reprovado
    #Média da curso 2
    media_curso2 = total_disciplinas_2 / quantidade_diciplina_2
    print("Media Total do curso 2:", media_curso2)
    print("Total de alunos no curso 2:", total_alunos_2)
    print("Total de Aprovados:", aprovado)
    print("Total de Reprovados:", reprovado)
    print("-----------------------")
else:
    media_curso2 = 0
    auxiliar_aprovado_2 = 0
    auxiliar_reprovado_2 = 0

#Média da faculdade
print("-----------------------")
faculdade_media = (media_curso1 + media_curso2) / 2
print("Somando a médias dos dois cursos, a média da faculdade tecfa é de:", faculdade_media)
print("Total de Aprovados:", auxiliar_aprovado_1 + auxiliar_aprovado_2)
print("Total de Reprovados:", auxiliar_reprovado_1 + auxiliar_reprovado_2)
print("-----------------------")
print("Agradeçemos por utilizar o sistema! :)")
print("-----------------------")
print("-----------------------")
print("Sistema desenvolvido por: Alan Paes ")

