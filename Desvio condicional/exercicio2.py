#Você está processo seletivo pra ser dev jr. E recebeu o teste para desenvolver. Será um processo para pizzaria, no qual receberá: nome do cliente, endereço, opções (mussarela, calabreza, portuguesa, marguerita), deverá imprimir o nome do cliente, endereço e sabor escolhido

#Passo 1. nome do cliente 
nome_do_cliente = input('Seja bem vindo! Qual e o seu nome por favor ?:')

#passo 2. endereço 
endereco = input("Endereço de entrega : ")

#passo 3. receber o pedido
pedido = input('Digite qual e o sabor para a sua pizza: \n (Mussarela | Calabreza | Portuguesa | Margueita) :')

print(f'Sr. {nome_do_cliente}, seu pedido será entregue no {endereco}, o sabor da escolhido é {pedido}')

#4. passo opções (elif traducão em pt-br senão então)
if pedido == 'Mussarela':
    print(f'Sr(a){nome_do_cliente}, o seu pedido  será entregue no {endereco}, sabor escolhido é: {pedido}')
elif pedido == 'Calabreza':
    print(f' Muito obrigado pelo seu pedido, {nome_do_cliente}. Nosso motoboy já está a caminho do {endereco}, com a sua pizza de {pedido}')
elif pedido == "Portuguesa":
    print(f'Exelente escolha {nome_do_cliente}, a nossa pizza {pedido} chegará em breve na {endereco}')
else:
    print(f'Oba! A pizza {pedido}, chegara quentinha na sua casa {endereco}, agradecemos pelo pedido {nome_do_cliente}')
