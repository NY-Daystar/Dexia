from . import GrandPrix


class Calendar:
    '''
    F1 Calendar in specific year
    '''
    year: str
    grand_prix: list[GrandPrix]

    def __init__(self, year=2023):
        self.year = year  # TODO trouver l'annee dans le scrapper
        self.grand_prix = []

    def add_grand_prix(self, g_prix: GrandPrix) -> None:
        '''Add grand prix in list'''
        self.grand_prix.append(g_prix)
