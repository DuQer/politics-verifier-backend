import requests
from base_sejm_api import BaseAPI

class ParliamentaryCommitteeData(BaseAPI):
    """Class to retrieve parliamentary committee data from the Sejm API."""

    def __init__(self, term=None, code=None, sum=None, num=None):
        """Initialize a new instance of ParliamentaryCommitteeData.

        Args:
            term (str): The term of the parliament office.
            code (str): The code of the committee.
            sum (str): The sum of committee details.
            num (str): The number of the committee sitting.
        """
        self.term = term
        self.code = code
        self.sum = sum
        self.num = num

    def get_committee_list(self):
        """Retrieve a list of all parliamentary committees for the specified term.

        Returns:
            dict: JSON data containing the list of committees, or None if the request failed.
        """
        url = f"{super().get_api()}{self.term}/committees"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
    
    def get_committee_details(self):
        """Retrieve details of a specific parliamentary committee for the specified term and code.

        Returns:
            dict: JSON data containing the details of the committee, or None if the request failed.
        """
        url = f"{super().get_api()}{self.term}/committees/{self.code}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
    
    def get_committee_sitting_list(self):
        """Retrieve a list of all sittings for a specific parliamentary committee for the specified term and code.

        Returns:
            dict: JSON data containing the list of sittings, or None if the request failed.
        """
        url = f"{super().get_api()}{self.term}/committees/{self.code}/sittings/{self.num}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
    
    def get_committee_sitting_details(self):
        """Retrieve details of a specific sitting for a parliamentary committee for the specified term, code, and number.

        Returns:
            dict: JSON data containing the details of the sitting, or None if the request failed.
        """
        url = f"{super().get_api()}{self.term}/committees/{self.code}/sittings/{self.num}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
    
    def get_committee_sitting_details_html(self):
        """Retrieve details of a specific sitting for a parliamentary committee in HTML format.

        Returns:
            str or None: HTML content of the sitting details, or None if the request failed.
        """
        url = f"{super().get_api()}{self.term}/committees/{self.code}/sittings/{self.num}/html"
        response = requests.get(url)
        return response.content if response.status_code == 200 else None
    
    def get_committee_sitting_recording_pdf(self):
        """Retrieve the recording of a specific sitting for a parliamentary committee in PDF format.

        Returns:
            bytes or None: PDF content of the sitting recording, or None if the request failed.
        """
        url = f"{super().get_api()}{self.term}/committees/{self.code}/sittings/{self.num}/pdf"
        response = requests.get(url)
        return response.content if response.status_code == 200 else None
