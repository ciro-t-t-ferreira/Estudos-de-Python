import re
#PROBLEMA NO VALIDA: ele aceita strings MAIORES do que o padrão
#Uso a variável padrão em mais de um método, preciso ver como estabelecer variáveis globais pra classe
class Telefone:
    def __init__(self, telefone):
        if self.valida(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número Inválido")
    def __str__(self):
        return self.format()

    def valida(self, telefone):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})" #Os '?' tornam o código de país opcional
        resultado = re.findall(padrao, telefone)
        if resultado: # Lista com elementos equivale a True, lista vazia equivale a False
            return True
        else:
            return False

    def format(self):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resultado = re.search(padrao, self.numero)
        numero_formatado = "+{}({}){}-{}".format(
            resultado.group(1),
            resultado.group(2),
            resultado.group(3),
            resultado.group(4))
        return numero_formatado