from validate_docbr import CPF
from validate_docbr import CNPJ

class documento:

    @staticmethod
    def cria_documento(doc):
        doc = str(doc)
        if (len(doc) == 11):
            return DocCPF(doc)
        if (len(doc) == 14):
            return DocCNPJ(doc)
        else:
            raise ValueError ("Documento inválido")

class DocCPF:

    def __init__(self, doc):
        doc = str(doc)
        if (self.valido(doc)):
            self.cpf = doc
            print("CPF Válido")
        else:
            raise ValueError("CPF inválido")

    def valido(self, doc):
        validador = CPF()  # ATENÇÃO!: essa é a classe importada do banco 'validate.dobr', não a que estão sendo criada aqui
        return validador.validate(doc)

    def format(self):
        mascara = CPF() #ATENÇÃO!: essa é a classe importada do banco 'validate.dobr', não a que estão sendo criada aqui
        return mascara.mask(self.cpf)
    def __str__(self):
        return self.format()

class DocCNPJ:

    def __init__(self, doc):
        doc = str(doc)
        if self.valido(doc):
            self.cnpj = doc
            print("CNPJ Válido")
        else:
            raise ValueError("CNPJ inválido")

    def valido(self, doc):
        validador = CNPJ()  # ATENÇÃO!: essa é a classe importada do banco 'validate.dobr', não a que estão sendo criada aqui
        return validador.validate(doc)

    def format(self):
        mascara = CNPJ() #ATENÇÃO!: essa é a classe importada do banco 'validate.dobr', não a que estão sendo criada aqui
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.format()