#calcule o preço de acordo com a tabela a seguir

kwh = float(input('Quantos kwh?'))
tipo = input('qual o tipo de instalação?')

if (tipo == 'R'):
    if kwh <= 500:
        preco = 0.4
    else:
        preco = 0.65

elif ( tipo == "C"):
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.6

elif (tipo == 'I'):
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.6
        print('instalação invalida')
print('total a pagar {}'.format(kwh * preco))

