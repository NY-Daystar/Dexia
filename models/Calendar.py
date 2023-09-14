from . import GrandPrix


class Calendar:
    """F1 Calendar in specific year"""    
    year: int
    grand_prix: list[GrandPrix]

    def __init__(self):
        self.grand_prix = []

    def add_grand_prix(self, g_prix: GrandPrix) -> None:
        '''Add grand prix in list'''
        self.grand_prix.append(g_prix)

    def set_year(self, year:int):
        """change year of calendar and for its Grand Prix

        
        Args:
            year (int): year to set for calendar and its Grand Prix
        """ 
        self.year = year 

        # Change year for every grand prix  
        [gp.set_year(year) for gp in self.grand_prix]

    def to_dict(self)-> dict[str, str]:
        """Convert object to dict for json serialization

        Returns:
            dict[str,str]: object in dict
        """        
        return {
            "year": self.year,
            "grand_prix": [gp.to_dict() for gp in self.grand_prix]
        }

    def __str__(self):
        return f'F1 calendar of {self.year} with {len(self.grand_prix)} Grand Prix'
