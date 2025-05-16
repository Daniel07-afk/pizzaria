#Você foi contratado pra criar um programa para uma autoescola, que deve verifica se a pessoa é maior ou tem 18 anos. Se ela tiver 18 ou mais, ela pode ter cnh, senão não pode dirigir.

#1. Receber o nome da pessoa
nome = input('Digite o seu nome:')
#2. Receber a idade da pessoa
idade = int(input('Digite a sua idade:'))
#3. possui cnh?
possui_cnh = input('Você possui a carteira de habilitatão ? \n (1-Sim / 2-Não):')

#4. verificar se a pessoa  >= 18
if idade >= 18:
    if possui_cnh == '1':
        print('maior de 18 anos e pode dirigir!')
    else:   
        print('não pode dirigir, não possui CNH')
else:
    print('menor de idade')