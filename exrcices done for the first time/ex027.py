#Exercício027
name = str(input('Qual é o seu nome completo?: ')).strip().title()
separa = name.split()
print('Seu primeiro nome é {}'.format(separa[0]))
print('Seu ultimo nome é {}'.format(separa[len(separa)-1]))
print('xD')
