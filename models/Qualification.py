from . import Event


class Qualification(Event):
    '''
    Qualifying Event
    '''
    def __init__(self, name, event_type, start_time):
        super().__init__(name, event_type, date=start_time)
