import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def __len__(self):
        return len(url)

    def __str__(self):
        return "URL:" + url + "\n" + "Parâmetros:" + self.get_url_parametros() + "\n" + "Base:" + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

    def sanitiza_url(self, url):
        return url.strip()

    def valida_url(self):
        if self.url == '':
            raise ValueError("A URL está vazia")
        
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        indice_interrogação = self.url.find('?')
        url_base = self.url[:indice_interrogação]
        return url_base

    def get_url_parametros(self):
        indice_interrogação = self.url.find('?')
        url_parametros = self.url[indice_interrogação + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e = self.get_url_parametros().find('&', indice_valor)
        if indice_e == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e]
        return valor

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")

valor_dolar = 5.50
moeda_or = extrator_url.get_valor_parametro("moedaOrigem")
moeda_des = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_or == "dolar":
    valor_final = float(quantidade) * valor_dolar
    print("R${:.2f}".format(valor_final))
else:
    valor_final = float(quantidade) / valor_dolar
    print("${:.2f}".format(valor_final))