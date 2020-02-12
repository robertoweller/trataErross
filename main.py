
try:

    x = '''


print '1234567891011121314151617181920'

print '0'

'''
    # Executa o texto.
    exec(x)

except SyntaxError as erro:
    # Retorna a mensagem de erro em str.
    mensage = erro.msg
    # retorna o print()...S2
    pri = erro.msg[53:64]
    # Me retorna o codigo errado em str
    texto = erro.text
    # Retorna a linha do erro em int
    linha = erro.lineno
    # Retorna quantas letras tem o codigo errado em int
    letras = erro.offset
    # retorna o que tipo é, tem que estudar + n entedi direito
    sla = erro.filename

    # Me retorna o print corrrigido, dentro da variavel test em forma de str.
    aaa = len(mensage)
    test = mensage[53:aaa-1] # Fatia a area do print('') junto com o texto entre ''

    # O erro tem 63 letras contando de 0.
    print(f'{test} é do tipo >> {type(test)} \n')
    print('-----------Apartir daqui o codigo corrigido------------------------')

    x = x.replace(texto, test)

    print(f'\n{x}')


# Deixa para executar o codigo depois
#    exec(x)
