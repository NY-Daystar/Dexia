from datetime import datetime

from .FreePractice import FreePractice
from .Qualification import Qualification
from .Race import Race
from . import EventType


class EventFactory:
    """EventFactory to instanciate Event object

    Returns:
        _type_: Event (Race, Qualifying, FreePractice)
    """
    name: str
    type: EventType
    start_date: datetime
    end_date: datetime

    @classmethod
    def create(cls, name: str, type: EventType, start_time: str, end_time: str):
        match type:
            case EventType.RACE:
                return Race(name, type, start_time, end_time)
            case EventType.QP:
                return Qualification(name, type, start_time, end_time)
            case EventType.FP1:
                return FreePractice(name, type, start_time, end_time)
            case EventType.FP2:
                return FreePractice(name, type, start_time, end_time)
            case EventType.FP3:
                return FreePractice(name, type, start_time, end_time)
            
            