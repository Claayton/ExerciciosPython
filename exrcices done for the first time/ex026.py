#Exercício026
frase = str(input('Digite uma frase: ')).strip().upper()
quantidade = frase.count('A')
print('Sua frase tem {} letras A.'.format(quantidade))
print('A primeira letra A apareceu na posição: {}'.format(frase.find('A') + 1))
print('A última letra A apareceu na posição: {}'.format(frase.rfind('A') + 1))
print('xD')
