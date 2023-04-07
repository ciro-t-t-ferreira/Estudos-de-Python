from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format()

    def mes_cadastro(self):
        meses_ano = ["janeiro", "fevereiro", "março", "abril",
                     "maio", "junho", "julho", "agosto",
                     "setembro", "outubro", "novembro", "dezembro"]
        mes_cadastro = self.momento_cadastro.month
        return meses_ano[mes_cadastro-1]

    def dia_semana(self):
        nomes_dias = ["segunda", "terça", "quarta", "quinta", "sexta",
                      "sábado", "domingo"]
        dia_semana = self.momento_cadastro.weekday()
        return nomes_dias[dia_semana]

    def format(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada