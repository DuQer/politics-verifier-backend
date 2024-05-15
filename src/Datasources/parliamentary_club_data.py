import requests
from base_sejm_api import BaseAPI

class ParliamentaryClubData(BaseAPI):
    """Class to retrieve parliamentary club data from the Sejm API."""

    def __init__(self, term=None, id=None):
        """Initialize a new instance of ParliamentaryClubData.

        Args:
            term (str): The term of the parliament office.
            id (str): The ID of the parliamentary club.
        """
        self.term = term
        self.id = id

    def get_list_of_parties(self):
        """Retrieve a list of all parliamentary clubs for the specified term.

        Returns:
            dict: JSON data containing the list of clubs, or None if the request failed.
        """
        url = f"{super().get_api()}{self.term}/clubs"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
    
    def get_party_details(self):
        """Retrieve details of a specific parliamentary club for the specified term and ID.

        Returns:
            dict: JSON data containing the details of the club, or None if the request failed.
        """
        url = f"{super().get_api()}{self.term}/clubs/{self.id}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

    def get_party_logo(self):
        """Retrieve the logo of a specific parliamentary club for the specified term and ID.

        Returns:
            bytes or None: Logo content of the club, or None if the request failed.
        """
        url = f"{super().get_api()}{self.term}/clubs/{self.id}"
        response = requests.get(url)
        return response.content if response.status_code == 200 else None
