from datetime import datetime
from dateutil.relativedelta import relativedelta


def calculate_driver_age(date_of_birth):
    return relativedelta(datetime.date(datetime.now()), datetime.strptime(date_of_birth,
                                                                          '%Y-%m-%d')).years
