import requests
from base_sejm_api import BaseAPI
    
class ParliamentDocuments(BaseAPI):
    """Class to retrieve parliament documents from the Sejm API."""

    def __init__(self, term=None, nr=None, fileName=None):
        """Initialize a new instance of ParliamentDocuments.

        Args:
            term (str): The term of the parliament office.
            nr (str): The number of the document.
            fileName (str): The file name of the document.
        """
        self.term = term
        self.nr = nr
        self.fileName = fileName
        
    def all_documents_list(self):
        """Retrieve a list of all documents available.

        Returns:
            dict: JSON data containing the list of documents, or None if the request failed.
        """
        url = f"{super().get_api()}/prints"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

    def specific_document_details(self):
        """Retrieve details of a specific document.

        Returns:
            dict: JSON data containing the details of the document, or None if the request failed.
        """
        url = f"{super().get_api()}/prints/{self.nr}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

    def get_document(self):
        """Retrieve the content of a specific document.

        Returns:
            bytes or None: PDF content of the document as bytes, or None if the request failed.
        """
        url = f"{super().get_api()}/{self.nr}/{self.fileName}"
        response = requests.get(url)
        return response.content if response.status_code == 200 else None
