import requests
from watcher_cli.services.auth_service import get_token

class APIClient:
    # Methods:
        # get()
        # post()
        # delete()
        # auto attach token headers
        # base URL from config

    # Handle errors:

        # timeout
        # unauthorized
        # network fail
    def __init__(self, base_url="http://localhost:8000/api"):
        self.base_url = base_url
        self.token = get_token()
    
    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.token}"}
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise Exception(f"GET request failed: {e}")
        except requests.exceptions.timeout:
            raise Exception("Get request timed out")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error: {e}")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise Exception("Unauthorized: Invalid or expired token")
            else:
                raise Exception(f"HTTP error: {e.response.status_code} - {e.response.text}")
    
    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.token}", "Content Type": "application/json"}
        try:
            response = requests.post(url, json=data, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise Exception(f"POST request failed: {e}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error: {e}")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise Exception("Unauthorized: Invalid or expired token")
            else:
                raise Exception(f"HTTP error: {e.response.status_code} - {e.response.text}")
            
    def delete(self,endpoint):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.token}"}
        try:
            response = requests.delete(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise Exception(f"Delte request failed: {e}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error: {e}")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise Exception("Unauthorized: Invalid or expired token")
            else:
                raise Exception(f"HTTP error: {e.response.status_code} - {e.response.text}")