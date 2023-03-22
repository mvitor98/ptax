import holidays
from typing import Iterable, Optional, Union

class HolidaysBr(holidays.BR):

    def __init__(self, 
                years: Optional[Union[int, Iterable[int]]] = None, 
                expand: bool = True, observed: bool = True, 
                subdiv: Optional[str] = None, 
                prov: Optional[str] = None, state: Optional[str] = None, 
                language: Optional[str] = None) -> None:
        super().__init__(years, expand, observed, subdiv, prov, state, language)
