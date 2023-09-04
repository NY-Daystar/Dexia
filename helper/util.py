from datetime import datetime


def get_date() -> str:
    '''Get date of now formatted like that (2023-09-04T10:21:05)'''
    date_time: datetime = datetime.now()
    return date_time.strftime("%Y-%m-%dT%H-%M-%S")
