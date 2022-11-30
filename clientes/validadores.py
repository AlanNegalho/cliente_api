from validate_docbr import CPF
import re

def validar_cpf(numero_cpf):
    cpf = CPF()
#    Validar CPF
#    cpf.validate("012.345.678-90") #True
#    if(len(numero_cpf) != 11):
    return cpf.validate(numero_cpf)

def validar_celular(numero_celular):
    #fazendo a verificaçao do numero
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo,numero_celular)
    return resposta