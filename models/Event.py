from datetime import datetime

from .enums import EventType

class Event:
    '''
    Event in Formula 1 (FP1, FP2, FP3, Qualifying, Race, Sprint)
    '''
    name: str
    type: EventType
    date: datetime

    def __init__(self, name: str, etype: EventType, date: datetime):
        self.name = name
        self.type = etype
        self.date = date

    def set_year(self, year: int) -> None:      
        self.date = self.date.replace(year=year)

    def __str__(self) -> str:
       return f'Type: {self.type.name} - Date - {self.date.strftime("%Y-%m-%dT%H:%M:%S")}'
