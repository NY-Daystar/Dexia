from datetime import datetime


def get_date() -> str:
    """ Get date of now formatted like that (2023-09-04)

    Returns:
        str: date in format %Y-%m-%dT%H-%M-%S
    """
    return datetime.now().strftime("%Y-%m-%d")
