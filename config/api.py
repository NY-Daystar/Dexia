class ApiConfig:
    '''Instance of ApiConfig'''
    host: str
    port: str

    def load(self, data: dict):
        '''Load config of Api'''
        if not data:
            return None
        self.port = data['port']
        self.host = data['host']
        return self
