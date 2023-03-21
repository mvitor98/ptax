import pandas as pd
from ptax import Ptax

ptax = Ptax()

period_ptax = ptax.get_period_ptax(start_date= "01-01-2023", end_date= "01-28-2023")
