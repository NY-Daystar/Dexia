from . import GrandPrix


class Calendar:
    """F1 Calendar in specific year"""    
    year: int
    version: int
    grand_prix: list[GrandPrix]

    def __init__(self):
        self.grand_prix = []

    def add_grand_prix(self, g_prix: GrandPrix) -> None:
        '''Add grand prix in list'''
        self.grand_prix.append(g_prix)

    def set_year(self, year:int):
        """Change year of calendar and for its Grand Prix
        Args:
            year (int): year to set for calendar and its Grand Prix
        """ 
        self.year = year 

        # Change year for every grand prix
        for gp in self.grand_prix:
            gp.set_year(year)

    def set_version(self, version:int):
        """Setter to set version of json document
        Args:
            version (int): version of the document 
        """ 
        self.version = version 

    def get_grand_prix(self, id:int) -> GrandPrix:
        """Get specific grand prix from its id
        Args:
            version (int): id of the grand prix in the calendar
        """ 
        try:
            return next(gp for gp in self.grand_prix if gp.index == id) 
        except IndexError as e:
            print(f'get_grand_prix exception: {e}')
            return None

    def to_dict(self)-> dict[str, str]:
        """Convert object to dict for json serialization

        Returns:
            dict[str,str]: object in dict
        """        
        return {
            "year": self.year,
            "version": self.version,
            "grand_prix": [gp.to_dict() for gp in self.grand_prix]
        }

    def __str__(self):
        return f'F1 calendar of {self.year} with {len(self.grand_prix)} Grand Prix'
