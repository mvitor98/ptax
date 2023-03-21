from datetime import datetime
from typing import Iterable
from brazilian_holidays import HolidaysBr


class DateValidator:

    def __cast_datetime(self, date) -> datetime.date:
        return datetime.strptime(date, '%m-%d-%Y')
    
    
    def __verify_weekend(self, date: datetime.date) -> bool:
        if self.weekday(date) not in (5, 6):
            return True
        
    def __holidays(self, date:str) -> Iterable:
        year = int(datetime.strftime(date, "%Y"))
        return HolidaysBr(years=year)
    
    def __verify_holiday(self, date: datetime.date) -> bool:
        if date not in self.__holidays(date):
            return True
        
    def verify_dates(self, start_date: str, end_date: str) -> bool:
        start_date, end_date = self.__cast_datetime(start_date), self.__cast_datetime(end_date)
        if start_date < end_date:
            raise ValueError("End date must be major than start date.")
        return True
    
    def verify_valid_date(self, date: str, ignore_weekend: bool = False) -> bool:
        
        if isinstance(date, str):
            date = self.__cast_datetime(date)

        if not ignore_weekend:
            if not self.__verify_weekend(date) or not self.__verify_holiday(date):
                raise ValueError("The date informed is in a weekend or is a holiday.")
        else:
            if not self.__verify_holiday(date):
                raise ValueError("The date informed is a holiday.")
        return True

    def weekday(self, date: datetime.date) -> int:
        return datetime.weekday(date)
