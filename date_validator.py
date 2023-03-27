from datetime import datetime, timedelta
from typing import Iterable
from brazilian_holidays import HolidaysBr
from calendar import isleap
from typing import Any, Union

class DateValidator:

    def __cast_datetime(self, date: Union[str,datetime.date], format: str= '%m-%d-%Y') -> datetime.date:
        if isinstance(date, str):
            try:
                date = datetime.strptime(date, format)
            except:
                raise ValueError("The date informed is invalid."\
                        "\nNote>>>> Take sure that the date is formatted like MM-DD-YYYY.")
        return date

    def __weekday(self, date: datetime.date) -> int:
        return datetime.weekday(date)
    
    def is_weekend(self, date: datetime.date) -> bool:
        if self.__weekday(self.__cast_datetime(date)) >= 5:
            return True
        
    def __holidays(self, date: datetime.date) -> Iterable:
        return HolidaysBr(years=date.year)
    
    def is_holiday(self, date: datetime.date) -> bool:
        if date in self.__holidays(date):
            return True
        
    def last_business_day(self, date:str = None) -> datetime.date:
        if not date:
            date = (datetime.today() - timedelta(days= 1)).strftime("%m-%d-%Y")

        if isinstance(date, str):
            date = self.__cast_datetime(date)

        if self.is_weekend(date):
            days_since_friday = (date.weekday() - 4) % 7
            last_friday = (date - timedelta(days=days_since_friday)).strftime("%m-%d-%Y")
            date = last_friday

        elif self.is_holiday(date):
            date = date - timedelta(days= 1)

        else:
            return date.strftime("%m-%d-%Y")

        return self.last_business_day(date)

    def verify_dates(self, start_date: str, end_date: str) -> None:
        start_date = self.__cast_datetime(start_date)
        end_date = self.__cast_datetime(end_date)

        if start_date > end_date:
            raise ValueError('Start date must me smaller than end date.')
        
        if start_date < (end_date - timedelta(days= 180)):
            raise ValueError("You can only consult 6 month range back in past.")
    
    def verify_date_input(self, date: Union[str, datetime.date]) -> None:
        if isinstance(date, str):
            date = self.__cast_datetime(date)
            
        minimum_date = datetime(year= 2000, month= 1, day= 3)
    
        if date < minimum_date:
            raise ValueError("You can only consult PTAX from date 01-03-2000 (jan-03-2000)."\
                             "\nNote>>>> Take sure that the date is formatted like MM-DD-YYYY.")
        
        if date > datetime.today():
            raise ValueError("Date must be less or equal today's date."\
                             "\nNote>>>> Take sure that the date is formatted like MM-DD-YYYY.")
        
        # if month > 12:
        #     raise ValueError("Month must be between 1 and 12.\nNote>>>> Take sure that the date is formatted like MM-DD-YYYY.")

        if not self.__is_in_month_days_limit(date):
            raise ValueError("The date informed is out of range of days at this month."\
                             "\nNote>>>> Take sure that the date is formatted like MM-DD-YYYY.")

        # if day <= 0 or day > 31:
        #     raise ValueError("Day must be between 1 and 31 as it's month max days.\nNote>>>> Take sure date is formatted like MM-DD-YYYY.")
        
    
    def __is_in_month_days_limit(self, date:datetime) -> bool:
        month = date.month
        day = date.day
        year = date.year
        mdl = {
            1: 31,
            2: [28 if not isleap(year) else 29][0],
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        if day <= mdl.get(month):
            return True            
        
