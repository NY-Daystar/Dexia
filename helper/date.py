from datetime import datetime


def get_datetime() -> str:
    """ Get date of now formatted like that (2023-09-04T10:21:05)

    Returns:
        str: date in format %Y-%m-%dT%H-%M-%S
    """    
    date_time: datetime = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    #return date_time

def get_date() -> str:
    """ Get date of now formatted like that (2023-09-04)

    Returns:
        str: date in format %Y-%m-%dT%H-%M-%S
    """    
    return datetime.now().strftime("%Y-%m-%d")