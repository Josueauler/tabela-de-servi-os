# tabela-de-servicos
tabela de cálculo de orçamentos para empreiteros - my first code.
#variaveis de serviços e valor m²
def pintura():
    try:
        valor_pintura=float(input('insira o valor da pintura por m² R$: '))
        mq=float(input('insira a área: '))
        resultado=mq*valor_pintura
        print('valor do serviço de pintura R$: {:.2f}.'.format(resultado))
    except ValueError:
        print('Erro. digite apenas números!')

pintura()

def eletrica():

    try:
        valor_eletrica=float(input('insira o valor da elétrica por m²: '))
        mq = float(input('insira a área: '))
        resultado = mq * valor_eletrica
        print('valor do serviço de elétrica R$: {:.2f}.'.format(resultado))
    except ValueError:
        print('Erro. digite apenas números.')

eletrica()

def alvenaria():

    try:
        valor_alvenaria=float(input('insira o valor da alvenaria por m²: '))
        mq = float(input('insira a área: '))
        resultado = mq * valor_alvenaria
        print('valor do serviço de alvenaria R$: {:.2f}.'.format(resultado))
    except ValueError:
        print('Erro. digite apenas números.')

alvenaria()

def encanamento():

    try:
        valor_encanamento = float(input('insira o valor da alvenaria por m²: '))
        mq = float(input('insira a área: '))
        resultado = mq * valor_encanamento
        print('valor do serviço de alvenaria R$: {:.2f}.'.format(resultado))
    except ValueError:
        print('Erro. digite apenas números.')

encanamento()
