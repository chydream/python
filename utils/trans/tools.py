from datetime import datetime
import random


def gen_trans_id(date=None):
    """
    :param date:
    :return:
    """
    if date is None:
        date = datetime.now()
    return date.strftime('%y%m%d%H%M%S%f') + str(random.randint(100000, 999999))