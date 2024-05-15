class BaseAPI:
    """Base class for API interactions."""

    BASE_URL = "https://api.sejm.gov.pl/sejm/"

    def __init__(self, BASE_URL):
        """Initialize a new instance of BaseAPI.

        Args:
            BASE_URL (str): The base URL of the API.
        """
        self.BASE_URL = BASE_URL

    def get_api(self):
        """Get the base URL of the API.

        Returns:
            str: The base URL of the API.
        """
        return self.BASE_URL
