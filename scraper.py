from urllib.error import HTTPError
import requests
from bs4 import BeautifulSoup, Tag, ResultSet

from helper.exc import BeautifulSoupException

from models import Calendar, GrandPrix


def scrap_calendar(url: str) -> Calendar:
    '''Scrap f1 calendar from url '''
    # TODO construire l'url au propre
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9
    }

    cookies = {
        # '_gat': '1',
        # '_gat_reworld_network': '1',
        # '_gat_oldTracker': '1',
        # '_gat_f1ireworld': '1',
        # '_gat_autojournal': '1',
    }

    response: requests.Response = requests.get(url, headers=headers, cookies=cookies)

    if not response.ok:
        raise HTTPError(url, response.status_code, "response not ok", headers, None)

    soup = BeautifulSoup(response.text, "html.parser")

    table: Tag = soup.find("table", class_={"calendar"})

    if table is None:
        raise BeautifulSoupException(url, 'Table tag with class \'calendar\' is not found')

    result_set: ResultSet[str] = table.find_all('tr')
    result_set.pop(0)  # Remove header

    return parse_calendar(result_set)


def parse_calendar(result_set: ResultSet) -> Calendar:
    calendar: Calendar = Calendar()

    for gp in result_set:
        elements = gp.find_all('td')
        index: str = elements[0].get_text()
        name: str = elements[1].get_text()
        date: str = elements[2].get_text()
        grand_prix: GrandPrix = GrandPrix(index, name, date)
        calendar.add_grand_prix(grand_prix)
    return calendar
