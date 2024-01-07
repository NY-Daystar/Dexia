from . import Event


class FreePractice(Event):
    '''
    FreePractice Event
    '''
    def __init__(self, name, type, start_time, end_time):
        super().__init__(name, type, start_time=start_time, end_time=end_time)