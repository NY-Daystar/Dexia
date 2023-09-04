from . import Type


class Event:
    '''
    Event in Formula 1 (FP1, FP2, FP3, Qualifying, Race, Sprint)
    '''
    name: str
    type: Type
    date: str
