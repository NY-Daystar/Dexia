import re
from datetime import datetime

from . import Event
from .enums import EventType, Month


class GrandPrix():
    '''
    F1 Grand prix
    '''
    index: int
    name: str

    '''Date of Grand Prix'''
    event: Event

    def __init__(self, index: str, name: str, date: str):
        self.index = int(index)
        self.name = name
        self.event = Event(name, EventType.GP, GrandPrix.extract_date(date))

    @classmethod
    def extract_date(cls, raw_date: str) -> datetime:
        """Extract date from french format

        Args:
            raw_date (str): raw date in this format (5 March)

        Returns:
            datetime: formatted date
        """
        regexp: re.Pattern = re.compile(r'(\d+)(er|ème)?\s([\wû]+)')
        match: re.Match[str] = regexp.match(raw_date)

        # si la date est déjà conforme
        if re.match(r"^\d{4}-\d{2}-\d{2}$", raw_date) is not None:
            return datetime.strptime(raw_date, "%Y-%m-%d")

        day: int = int(match.group(1))
        month: int = int(Month[match.group(3).upper()])

        return datetime(day=day, month=month, year=9999)

    def add_event(self, event: Event) -> None:
        """Add a new event in Grand Prix

        Args:
            event (Event): event to add
        """
        self.events.append(event)

    def set_year(self, year: int) -> None:
        self.event.set_year(year)

    def to_dict(self) -> dict[str, str]:
        """Convert object to dict for json serialization

        Returns:
            dict[str,str]: object in dict
        """
        return {
            "index": self.index,
            "name": self.name,
            "date": self.event.date.strftime('%Y-%m-%d')
        }

    def __str__(self) -> str:
        return f'Index: {self.index} - Name: {self.name} - {self.event}'
