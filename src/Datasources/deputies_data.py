import requests
from base_sejm_api import BaseAPI

class DeputiesData(BaseAPI):
    """Class to retrieve deputies data from the Sejm API."""

    def __init__(self, term=None, leg=None, sitting=None, date=None):
        """Initialize a new instance of DeputiesData.

        Args:
            term (str): The term of parliament office.
            leg (str): The deputy ID number.
            sitting (int): The number of the parliament session.
            date (str): The date of voting in the format 'yyyy-mm-dd'.
        """
        self.term = term
        self.leg = leg
        self.sitting = sitting
        self.date = date

    def get_all_deputies(self):
        """Retrieve data of all deputies for the specified term.

        Returns:
            dict: JSON data containing the data of all deputies, or None if the request failed.
        """
        url = f"{super().get_api()}{self.term}/MP"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

    def get_deputy_data(self):
        """Retrieve data of a specific deputy for the specified term and deputy ID.

        Returns:
            dict: JSON data containing the data of the specific deputy, or None if the request failed.
        """
        url = f"{super().get_api()}{self.term}/MP/{self.leg}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

    def get_deputy_photo(self):
        """Retrieve the photo of a specific deputy for the specified term and deputy ID.

        Returns:
            dict: JSON data containing the photo of the specific deputy, or None if the request failed.
        """
        url = f"{super().get_api()}{self.term}/MP/{self.leg}/photo"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

    def get_deputy_photo_min(self):
        """Retrieve the mini photo of a specific deputy for the specified term and deputy ID.

        Returns:
            dict: JSON data containing the mini photo of the specific deputy, or None if the request failed.
        """
        url = f"{super().get_api()}{self.term}/MP/{self.leg}/photo-mini"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

    def get_deputy_voting_data(self):
        """Retrieve voting data of a specific deputy for the specified term, session, and date.

        Returns:
            dict: JSON data containing the voting data of the specific deputy, or None if the request failed.
        """
        url = f"{super().get_api()}{self.term}/MP/{self.leg}/votings/{self.sitting}/{self.date}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
