import requests
from datetime import datetime, date

class Heathrow():

    def __init__(self):

        self.code = 'LHR'
        self.full_name = 'London Heathrow'

        self.arrivals_session = requests.Session()
        self.arrivals_session.get('https://www.heathrow.com/arrivals')
        self.last_arrivals_request = datetime.now()

        self.departures_session = requests.Session()
        self.departures_session.get('https://www.heathrow.com/departures')
        self.last_departures_request = datetime.now()

    def arrivals(self):

        # Refresh the session if it's been more than an hour since the last request
        if (datetime.now() - self.last_arrivals_request).seconds > 3600:
            self.arrivals_session = requests.Session()
            self.arrivals_session.get('https://www.heathrow.com/arrivals')
            self.last_arrivals_request = datetime.now()

        params = {
            'date': date.today().strftime('%Y-%m-%d'),
            'orderBy': 'localArrivalTime',
            'excludeCodeShares': True,
        }

        headers = {
            'Origin': 'https://www.heathrow.com',
        }

        response = self.arrivals_session.get(
            'https://api-dp-prod.dp.heathrow.com/pihub/flights/arrivals',
            params=params,
            headers=headers
            )

        return response.json()

    def departures(self):

        # Refresh the session if it's been more than an hour since the last request
        if (datetime.now() - self.last_departures_request).seconds > 3600:
            self.departures_session = requests.Session()
            self.departures_session.get('https://www.heathrow.com/departures')
            self.last_departures_request = datetime.now()

        params = {
            'date': date.today().strftime('%Y-%m-%d'),
            'orderBy': 'localArrivalTime',
            'excludeCodeShares': True,
        }

        headers = {
            'Origin': 'https://www.heathrow.com',
        }

        response = self.departures_session.get(
            'https://api-dp-prod.dp.heathrow.com/pihub/flights/departures',
            params=params,
            headers=headers
            )

        return response.json()