import random
nome1=input("Digite o nome do aluno: ")
nome2=input('Digite o nome do segundo aluno: ')
nome3=input('Digite o nome do terceiro aluno: ')
nome4= input('Digite o nome do quarto aluno: ')
Lista= {nome1, nome2, nome3, nome4}
escolhido= random.choice(Lista)
print('O aluno escolhido foi:{}'.format (escolhido))