from pprint import pprint
import requests as rq
from datetime import datetime
from brazilian_holidays import HolidaysBr
from typing import Dict, Optional, Union, Iterable

class Ptax:

    def __init__(self, year:int) -> None:
        self.year = year
        
    def __cast_datetime(self, date) -> datetime.date:
        return datetime.strptime(date, '%m-%d-%Y')

    def __weekday(self, date: datetime.date) -> int:
        return datetime.weekday(date)
    
    @property
    def holidays(self) -> Iterable:
        return HolidaysBr(years=self.year)

    def get_ptax(self, date) -> Dict:
        if self.__verify_valid_date(date):
            url_base = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{date}'&$top=100&$format=json"
            response = rq.get(url_base)
            return response.json()

    def __verify_weekend(self, date: datetime.date) -> bool:
        if self.__weekday(date) not in (5, 6):
            return True
    
    def __verify_holiday(self, date: datetime.date) -> bool:
        if date not in self.holidays:
            return True
        
    def __verify_valid_date(self, date: str) -> bool:
        date = self.__cast_datetime(date)
        if not self.__verify_weekend(date) or not self.__verify_holiday(date):
            raise ValueError("The date informed is in a weekend or is a holiday.")
        return True


if __name__ == "__main__":
    
    date = "10-14-2022"

    ptax = Ptax(int(date[6:])).get_ptax(date)

    pprint(ptax)
