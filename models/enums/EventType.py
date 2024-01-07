from enum import Enum


class EventType(Enum):
    '''
    Type of event
    '''
    UNKNOWN = 0
    GP = 1
    FP1 = 2
    FP2 = 3
    FP3 = 4
    QP = 5
    RACE = 6
