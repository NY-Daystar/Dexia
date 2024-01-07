class BeautifulSoupException(Exception):
    '''Exception when scrap doesn't find tag'''

    def __init__(self, url: str, message: str):
        self.url = url
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Url: {self.url} - Message: {self.message}"
