from .urls import URLs
import requests


class FetchResponse(object):

    def __init__(self):
        self.url = URLs()

    def fetch_legislation_response(self, **payload):

        parameters = (payload['bill_status'], payload['bill_source'], payload['date_start'], payload['skip'],
                      payload['limit'], payload['member_id'], payload['bill_id'], payload['bill_no'],
                      payload['bill_year'])
        try:
            response = requests.request('GET', self.url.legislation_url(), params=payload)

            response.raise_for_status()
        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        return response

    def fetch_debate_response(self, **kwargs):
        try:
            response = requests.request('GET', self.url.debate_url())

            response.raise_for_status()
        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        return response

    def fetch_constituencies_response(self, **kwargs):
        try:
            response = requests.request('GET', self.url.constituencies_url())

            response.raise_for_status()
        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        return response

    def fetch_parties_response(self, **kwargs):
        try:
            response = requests.request('GET', self.url.parties_url())

            response.raise_for_status()
        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        return response

    def fetch_divisions_response(self, **kwargs):
        try:
            response = requests.request('GET', self.url.divisions_url())

            response.raise_for_status()
        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        return response

    def fetch_questions_response(self, **kwargs):
        try:  
            response = requests.request('GET', self.url.questions_url())

            response.raise_for_status()
        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        return response

    def fetch_houses_response(self, **kwargs):
        try:
            response = requests.request('GET', self.url.houses_url())

            response.raise_for_status()
        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        return response

    def fetch_members_response(self, **kwargs):
        try:
            response = requests.request('GET', self.url.members_url())

            response.raise_for_status()
        except requests.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        return response


class FetchData(FetchResponse):

    def __init__(self):
        super().__init__()

    def fetch_legislation(self, **kwargs):
        response = self.fetch_legislation_response(**kwargs)

        return response
