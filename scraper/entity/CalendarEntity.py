
'''Module to scrap data about F1 calendar'''
import re
from urllib.error import HTTPError

from bs4 import BeautifulSoup, ResultSet, Tag
from requests import Response

from helper import get_mp_logger, request
from helper.exc import BeautifulSoupException
from models import Calendar, GrandPrix

from . import Entity

log = get_mp_logger()


class CalendarEntity(Entity):
    """Entity which handles f1 calendar scrapping

    Args:
        Entity (_type_): generic entity
    """

    def scrap(self, url: str) -> Calendar:
        """Scrap f1 calendar from url

        Args:
            url (str): url to scrap 

        Raises:
            BeautifulSoupException: _description_

        Returns:
            Calendar: Calendar Model
        """
        log.debug('Url to scrap for Calendar: %s', url)
        response: Response

        try:
            response: Response = request(url)
        except HTTPError as exc:
            log.error('Http error thrown %s', exc)
            return None
        except Exception as exc:
            log.error('Exception thrown %s', exc)
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        table: Tag = soup.find("table", class_={"calendar"})

        if table is None:
            raise BeautifulSoupException(url, 'Table tag with class \'calendar\' is not found')

        result_set: ResultSet[str] = table.find_all('tr')

        return self.parse(result_set)

    def parse(self, result_set: ResultSet) -> Calendar:
        """Parse resultSet to get a Calendar model

        Args:
            result_set (ResultSet): data scrap from url before

        Returns:
            Calendar: Calendar model
        """

        calendar: Calendar = Calendar()
        result_set.pop(0)  # Remove the headers

        for gp in result_set:
            elements = gp.find_all('td')
            index: str = elements[0].get_text()
            name: str = elements[1].get_text()
            date: str = elements[2].get_text()

            log.debug('index: %s - name: %s - date: %s', index, name, date)
            grand_prix: GrandPrix = GrandPrix(index, name, date)
            calendar.add_grand_prix(grand_prix)
        return calendar

    def scrap_year(self, url: str) -> int:
        """Scrap year of F1 calendar

        Args:
            url (str): url to scrap 

        Returns:
            int: year of the calendar
        """
        return int(re.findall(r'\d{4}', url)[0])
