import re
import typing
from datetime import datetime

from . import Qualification
from . import Race
from . import Month


class GrandPrix(typing.Protocol):
    '''
    F1 Grand prix
    '''
    NAME: str
    index: int
    name: str
    date: str
    qualification: Qualification
    race: Race
    HIGH = 25

    def __init__(self, index: str, name: str, date: str, high=HIGH):
        self.index = int(index)
        self.name = name
        self.date = GrandPrix.extract_date(date)

    @classmethod
    def extract_date(cls, raw_date: str) -> datetime:
        '''Extract date from french format'''

        regexp: re.Pattern = re.compile(r'(\d+)\s([\w]+)')
        match: re.Match[str] = regexp.match(raw_date)

        day: int = int(match.group(1))
        month: int = int(Month[match.group(2).upper()])

        # TODO recuperer l'annee
        return datetime(day=day, month=month, year=2023)

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < self.HIGH:
            return self.index
        raise StopIteration

    def __str__(self) -> str:
        return f'index: {self.index} - name: {self.name} - date: {datetime.strftime(self.date, "%Y-%m-%d")}'
