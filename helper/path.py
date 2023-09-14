"""Helper to handle path"""
from os.path import join
from pathlib import Path


def path_combine(*args)-> Path:
    """Combine path give in arguments   

    Returns:
        Path: path combined
    """
    return Path(join(*args)) 

