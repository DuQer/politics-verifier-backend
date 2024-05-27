import requests
from base_sejm_api import BaseAPI

class TermOfOfficeData(BaseAPI):
    """Class to retrieve term of office data from the Sejm API."""

    def __init__(self, term=None):
        """Initialize a new instance of TermOfOfficeData.

        Args:
            term (str): The term of the parliament office.
        """
        self.term = term

    def get_all_terms(self):
        """Retrieve a list of all terms of office.

        Returns:
            dict: JSON data containing the list of terms, or None if the request failed.
        """
        url = f"{super().get_api()}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

    def get_term(self):
        """Retrieve details of a specific term of office.

        Returns:
            dict: JSON data containing the details of the term, or None if the request failed.
        """
        url = f"{super().get_api()}/{self.term}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
