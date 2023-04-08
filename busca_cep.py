import requests
"""
Sobre a biblioteca, ver o link: https://requests.readthedocs.io/en/latest/
"""

class BuscaCep:

    def __init__(self,cep):
        cep = str(cep)
        if self.validate:
            self.cep = cep
        else:
            raise ValueError("CEP inválido")

    def __str__(self):
        return self.format()

    def validate(self, cep):
        cep = str(cep)
        if (len(cep) == 8):
            return True
        else:
            return False

    def format(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url) #essa função "pega" informações do link do argumento
        dados = r.json() #Organiza o conteúdo do link obtido pelo get em dicionário
        return (
            dados["bairro"],
            dados["localidade"],
            dados["uf"]
        )
