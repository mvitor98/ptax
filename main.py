from ptax import Ptax
import argparse
from date_validator import DateValidator
from datetime import datetime


parser = argparse.ArgumentParser("PTAX date selector. If no args, it will return the last PTAX recorded.")
parser.add_argument("-d", "--date", default=None, type=str, 
                    help="Type a DATE to search for a PTAX. (MM-DD-YYYY)")
parser.add_argument("-sd", "--startDate", default=None, type=str, 
                    help="Type a START date to search for PTAX. (MM-DD-YYYY)")
parser.add_argument("-ed", "--endDate", default=None, type=str, 
                    help="Type a END date to search for PTAX. (MM-DD-YYYY)")
args = parser.parse_args()


if __name__ == "__main__":
    
    ptax = Ptax()
    dv = DateValidator()
    
    dates = {
        "start_date": args.startDate,
        "end_date": args.endDate,
        "date": args.date
    }
 
    start_date = dates.get("start_date")
    end_date = dates.get("end_date")
    date = dates.get("date")
 
    for _, v in dates.items():
        if v:
            dv.verify_date_input(v)

    if start_date and end_date:
        dv.verify_dates(start_date= start_date, end_date= end_date)
        currency = ptax.get_period_ptax(start_date= start_date, end_date= end_date)

    elif date:
        currency = ptax.get_day_ptax(dv.last_business_day(date))
    
    else:
        parser.print_help()
        print("\n\n")
        date = dv.last_business_day()
        currency = ptax.get_day_ptax(dv.last_business_day())

    print(currency)
