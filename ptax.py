import pandas as pd
import requests as rq
from typing import Dict

class Ptax:

    def __init__(self) -> None:
        self.__base_url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
    
    def get_day_ptax(self, date: str) -> Dict:
        endpoint = "CotacaoDolarDia(dataCotacao=@dataCotacao)"
        query = f"?@dataCotacao='{date}'&$top=100&$format=json"
        url = self.__base_url + endpoint + query
        response = rq.get(url)
        return pd.DataFrame(response.json().get("value"))

    def get_period_ptax(self, start_date:str, end_date:str) -> Dict:
        endpoint = "CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"
        query = f"?@dataInicial='{start_date}'&@dataFinalCotacao='{end_date}'&$top=100&$format=json"
        url = self.__base_url + endpoint + query
        response = rq.get(url)
        return pd.DataFrame(response.json().get("value"))
