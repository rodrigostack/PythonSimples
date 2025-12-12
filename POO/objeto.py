class people:
    nome = ""
    idade = 0
    cor = ""
    altura = 0

pessoa1 = people()
pessoa1.nome = input("Digite o nome da pessoa:\n")
pessoa1.idade = int(input("Digite a idade:\n"))
pessoa1.cor = input("Digite a cor:\n")
pessoa1.altura = float(input("Digite a altura:\n"))

print("Seu nome é", {pessoa1.nome} ,"sua idade é" ,{pessoa1.idade})