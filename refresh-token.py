try:
    import requests
except ImportError:
    import urequests as requests

import credentials


class Refresh:
    def __init__(self, refresh_token, client_id, client_secret):
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret

    def refresh(self):
        url = "https://accounts.spotify.com/api/token"
        data = "&".join(
            [
                "grant_type=refresh_token",
                f"refresh_token={self.refresh_token}",
                f"client_id={self.client_id}",
                f"client_secret={self.client_secret}",
            ]
        )
        print(data)

        headers = {
            "content-type": "application/x-www-form-urlencoded",
        }

        response = requests.post(url, data=data, headers=headers)

        print(response.status_code)
        print(response.reason)
        print(response.text)


a = Refresh(credentials.refresh_token, credentials.client_id, credentials.client_secret)
a.refresh()
