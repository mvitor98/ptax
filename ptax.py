import requests as rq
from typing import Dict
from date_validator import DateValidator

class Ptax:

    date_validator = DateValidator()

    def __init__(self) -> None:
        self.__base_url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
    
    def get_day_ptax(self, date: str) -> Dict:
        if self.date_validator.verify_valid_date(date):
            endpoint = "CotacaoDolarDia(dataCotacao=@dataCotacao)"
            query = f"?@dataCotacao='{date}'&$top=100&$format=json"
            url = self.__base_url + endpoint + query
            response = rq.get(url)
            return response.json().get("value")[0]

    def get_period_ptax(self, start_date:str, end_date:str) -> Dict:
        if self.date_validator.verify_dates(start_date, end_date):
            endpoint = "CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"
            query = f"?@dataInicial='{start_date}'&@dataFinalCotacao='{end_date}'&$top=100&$format=json"
            url = self.__base_url + endpoint + query
            response = rq.get(url)
            return response.json().get("value")


if __name__ == "__main__":
    
    date = "10-14-2022"

    ptax = Ptax()
    day = ptax.get_day_ptax(date)
    period = ptax.get_period_ptax(start_date= "10-01-2022", end_date= "10-31-2022")
    print(*period, sep= "\n")
