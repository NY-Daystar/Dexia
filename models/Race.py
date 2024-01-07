from . import Event

class Race(Event):
    '''
    Race event
    '''
    def __init__(self, name, type, start_time, end_time):
        super().__init__(name, type, start_time=start_time, end_time=end_time)