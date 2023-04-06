from validate_docbr import CPF

class cpf:

    def __init__(self, doc):
        doc = str(doc)
        if self.validacao_cpf(doc):
            self.cpf = doc
            print("CPF Válido")
        else:
            raise ValueError("CPF inválido")

    #Separa erro de número incorreto de dígitos de outros possíveis erros
    def validacao_cpf(self, doc): #Verifica se tem o número correto de dígitos
        if len(doc) == 11:
            validador = CPF() #ATENÇÃO!: essa é a classe importada do banco 'validate.dobr', não a que estão sendo criada aqui
            return validador.validate(doc) #Método da bib 'validate_docbr', retorna True pra formato válido e False para inválido
        else:
            raise ValueError("Número inválido de dígitos")

    def format_cpf(self):
        mascara = CPF() #ATENÇÃO!: essa é a classe importada do banco 'validate.dobr', não a que estão sendo criada aqui
        return mascara.mask(self.cpf)

    #def format_cpf(self):
        part1 = self.cpf[:3]
        part2 = self.cpf[3:6]
        part3 = self.cpf[6:9]
        part4 = self.cpf[9:]
        return (f"{part1}.{part2}.{part3}-{part4}")
