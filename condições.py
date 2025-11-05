aluno = input("informe o nome do aluno:\n")
nota1 = float(input("Digite a 1ª nota\n"))
nota2 = float(input("Digite a 2ª nota\n"))
nota3 = float(input("Digite a 3ª nota\n"))
nota4 = float(input("Digite a 4ª nota\n"))

média = (nota1 + nota2 + nota3 + nota4) / 4

if média >= 6.5:
    print("O aluno", aluno, "esta APROVADO")
else:
    print("O aluno", aluno, "esta REPROVADO")