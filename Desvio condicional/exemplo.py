nome = input('digite o seu nome:')
idade = int(input('digite a sua idade:'))

#if e SE em pt-br e else é SENÃO
if idade >= 18:
    print('Autorizado, maior de idade', idade)
else:
    print(f'não autorizado, menor de idade: {idade} anos')
