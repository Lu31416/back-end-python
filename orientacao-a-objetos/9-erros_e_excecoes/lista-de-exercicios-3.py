## O programa abaixo deve calcular a média dos valores digitados pelo usuário.
## No entanto, ele não está funcionando bem. Você pode consertá-lo?

def calcular_media(valores):
    tamanho = len(valores)
    soma = sum(valores)
    media = soma / tamanho
    return media

continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    if valor.lower() == 'ok':
        continuar = False
    else:
        try:
            valor = float(valor)
            valores.append(valor)
        except ValueError:
            print('Valor inválido. Por favor, insira um número válido.')

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores, media))