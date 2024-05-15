import requests
from base_sejm_api import BaseAPI

class VotingData(BaseAPI):
    """Class to retrieve voting data from the Sejm API."""

    def __init__(self, term=None, sitting=None, voting_num=None, leg=None, date=None):
        """Initialize a new instance of VotingData.

        Args:
            term (str): The term of parliament office.
            sitting (int): The number of the parliament session.
            voting_num (int): The number of the voting.
            leg (str): The deputy ID number.
            date (str): The date of voting in the format 'yyyy-mm-dd'.
        """
        self.term = term
        self.sitting = sitting
        self.voting_num = voting_num
        self.leg = leg
        self.date = date

    def votings_list(self):
        """Retrieve a list of all votings for the specified term and sitting.

        Returns:
            dict: JSON data containing the list of votings, or None if the request failed.
        """
        url = f"{super().get_api()}{self.term}/votings/{self.sitting}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

    def voting_details(self):
        """Retrieve details of a specific voting for the specified term, sitting, and voting number.

        Returns:
            dict: JSON data containing the voting details, or None if the request failed.
        """
        url = f"{super().get_api()}{self.term}/votings/{self.sitting}/{self.voting_num}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

    def deputy_voting(self):
        """Retrieve voting data for a specific deputy for the specified term, sitting, and date.

        Returns:
            dict: JSON data containing the deputy's voting data, or None if the request failed.
        """
        url = f"{super().get_api()}{self.term}/MP/{self.leg}/votings/{self.sitting}/{self.date}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
