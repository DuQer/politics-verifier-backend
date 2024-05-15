import requests
from base_sejm_api import BaseAPI

class ParliamentBroadcasts(BaseAPI):
    """Class to retrieve parliament broadcasts data from the Sejm API."""

    def __init__(self, term=None):
        """Initialize a new instance of ParliamentBroadcasts.

        Args:
            term (str): The term of the parliament office.
        """
        self.term = term

    def get_broadcasts_list(self):
        """Retrieve a list of all parliament broadcasts for the specified term.

        Returns:
            dict: JSON data containing the list of broadcasts, or None if the request failed.
        """
        url = f"{super().get_api()}{self.term}/videos"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

    def get_broadcasts_today(self):
        """Retrieve parliament broadcasts scheduled for today for the specified term.

        Returns:
            dict: JSON data containing the broadcasts scheduled for today, or None if the request failed.
        """
        url = f"{super().get_api()}{self.term}/videos/today"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
