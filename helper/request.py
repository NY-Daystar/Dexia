from urllib.error import HTTPError

from requests import Response, get


def request(url: str) -> Response:
    """Send HTTP type GET request with appropriate headers 

    Args:
        url (str): url to request in HTTP GET

    Returns:
        Response: HTTP Response
    """ 

    headers: dict = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
    }

    cookies: dict = {
        '_gat': '1',
        '_gat_reworld_network': '1',
        '_gat_oldTracker': '1',
        '_gat_f1ireworld': '1',
        '_gat_autojournal': '1',
    }

    response: Response =  get(url, headers=headers, cookies=cookies)

    if not response.ok:
        raise HTTPError(url, response.status_code, response.content, response.headers, response.content)

    return response
