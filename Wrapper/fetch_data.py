import logging

from .urls import URLs
import requests


#Fetches response from the relevant endpoints and applies paramters are needed
#Default response is just the HTTP Code
class FetchResponse(object):

    def __init__(self):
        self.url = URLs()

    #Fetches a response from the legislation API endpoint
    def fetch_legislation_response(self, params: dict) -> dict:
        #Assinged the response variable before entering the try/except loop
        response = None

        logging.debug(msg=f'Fetching response from legislation endpoint with params: {params}')
        try:
            response = requests.request('GET', self.url.legislation_url(), params=params)

            response.raise_for_status()
        except requests.HTTPError as http_err:
            logging.error(msg=http_err)
        except Exception as err:
            logging.error(msg=err, exc_info=True)

        logging.debug(msg=f'Response from {self.url.legislation_url()}: {response}')
        return response

    #Fetches a response from the debate API endpoint
    def fetch_debate_response(self, params: dict) -> dict:
        #Assinged the response variable before entering the try/except loop
        response = None

        logging.debug(msg=f'Fetching response from debate endpoint with params: {params}')
        try:
            response = requests.request('GET', self.url.debate_url(), params=params)

            response.raise_for_status()
        except requests.HTTPError as http_err:
            logging.error(msg=http_err)
        except Exception as err:
            logging.error(msg=err, exc_info=True)

        logging.debug(msg=f'Response from {self.url.debate_url()}: {response}')
        return response

    #Fetches a response from the constituencies API endpoint
    def fetch_constituencies_response(self, params: dict) -> dict:
        #Assinged the response variable before entering the try/except loop
        response = None

        constituencies_params = {'chamber_id':''}
        constituencies_params.update(params)

        logging.debug(msg=f'Fetching response from constituencies endpoint with params: {constituencies_params}')
        try:

            response = requests.request('GET', self.url.constituencies_url(), params=constituencies_params)

            response.raise_for_status()
        except requests.HTTPError as http_err:
            logging.error(msg=http_err)
        except Exception as err:
            logging.error(msg=err, exc_info=True)

        logging.debug(msg=f'Response from {self.url.constituencies_url()}: {response}')
        return response

    #Fetches a response from the parties API endpoint
    def fetch_parties_response(self, params: dict) -> dict:
        #Assinged the response variable before entering the try/except loop
        response = None

        logging.debug(msg=f'Fetching response from parties endpoint with params: {params}')
        try:
            response = requests.request('GET', self.url.parties_url(), params=params)

            response.raise_for_status()
        except requests.HTTPError as http_err:
            logging.error(msg=http_err)
        except Exception as err:
            logging.error(msg=err, exc_info=True)

        logging.debug(msg=f'Response from {self.url.parties_url()}: {response}')
        return response

    #Fetches a response from the divisions API endpoint
    def fetch_divisions_response(self, params: dict) -> dict:
        #Assinged the response variable before entering the try/except loop
        response = None

        try:
            response = requests.request('GET', self.url.divisions_url(), params=params)

            response.raise_for_status()
        except requests.HTTPError as http_err:
            logging.error(msg=http_err)
        except Exception as err:
            logging.error(msg=err, exc_info=True)
        return response

    #Fetches a response from the questions API endpoint
    def fetch_questions_response(self, params: dict) -> dict:
        #Assinged the response variable before entering the try/except loop
        response = None

        logging.debug(msg=f'Fetching response from questions endpoint with params: {params}')
        try:  
            response = requests.request('GET', self.url.questions_url(), params=params)

            response.raise_for_status()
        except requests.HTTPError as http_err:
            logging.error(msg=http_err)
        except Exception as err:
            logging.error(msg=err, exc_info=True)

        logging.debug(msg=f'Response from {self.url.questions_url()}: {response}')
        return response

    #Fetches a response from the houses API endpoint
    def fetch_houses_response(self, params: dict) -> dict:
        #Assinged the response variable before entering the try/except loop
        response = None

        logging.debug(msg=f'Fetching response from houses endpoint with params: {params}')
        try:
            response = requests.request('GET', self.url.houses_url(), params=params)

            response.raise_for_status()
        except requests.HTTPError as http_err:
            logging.error(msg=http_err)
        except Exception as err:
            logging.error(msg=err, exc_info=True)

        logging.debug(msg=f'Response from {self.url.houses_url()}: {response}')
        return response

    #Fetches a response from the members API endpoint
    def fetch_members_response(self, params: dict) -> dict:
        #Assinged the response variable before entering the try/except loop
        response = None

        logging.debug(msg=f'Fetching response from members endpoint with params: {params}')
        try:
            response = requests.request('GET', self.url.members_url(), params=params)

            response.raise_for_status()
        except requests.HTTPError as http_err:
            logging.error(msg=http_err)
        except Exception as err:
            logging.error(msg=err, exc_info=True)

        logging.debug(msg=f'Response from {self.url.members_url()}: {response}')
        return response

#Returns data content from the data responses
class FetchData(FetchResponse):

    def __init__(self):
        super().__init__()


    #Returns the contents of the legislation data from the API endpoint
    def fetch_legislation_data(self, params: dict) -> dict:
        #Assinged the response variable before entering the try/except loop
        response = None

        logging.info(msg=f'Fetching response from legislation endpoint with params: {params}')
        try:
            response = self.fetch_legislation_response(params)
            response = response.json()
            logging.debug(msg=f'Response from {self.url.legislation_url()} as {response}')
        except Exception as err:
            logging.error(msg=err, exc_info=True)
        finally:
            logging.info(f'Returning data from request: {self.url.legislation_url()}, with params: {params}')
            return response

    #Returns the contents of the questions data from the API endpoint
    def fetch_questions_data(self, params: dict) -> dict:
        #Assinged the response variable before entering the try/except loop
        response = None

        logging.info(msg=logging.debug(msg=f'Fetching response from questions endpoint with params: {params}'))
        try:
            response = self.fetch_questions_response(params)
            response = response.json()
            logging.debug(msg=f'Response from {self.url.questions_url()} was: {response}')
        except Exception as err:
            logging.error(msg=err, exc_info=True)
        finally:
            logging.info(f'Returning data from request: {self.url.questions_url()}, with params: {params}')
            return response

    #Returns the contents of the debate data from the API endpoint
    def fetch_debate_data(self, params: dict) -> dict:
        #Assinged the response variable before entering the try/except loop
        response = None

        logging.info(msg=logging.debug(msg=f'Fetching response from debate endpoint with params: {params}'))
        try:
            response = self.fetch_debate_response(params)
            response = response.json()
            logging.debug(msg=f'Response from {self.url.debate_url()} was: {response}')
        except Exception as err:
            logging.error(msg=err, exc_info=True)
        finally:
            logging.info(f'Returning data from request: {self.url.debate_url()}, with params: {params}')
            return response

    #Returns the contents of the contituencies data from the API endpoint
    def fetch_constituencies_data(self, params: dict) -> dict:
        #Assinged the response variable before entering the try/except loop
        response = None

        logging.info(msg=logging.debug(msg=f'Fetching response from constituencies endpoint with params: {params}'))
        try:
            response = self.fetch_constituencies_response(params)
            response = response.json()
            logging.debug(msg=f'Response from {self.url.constituencies_url()} was: {response}')
        except Exception as err:
            logging.error(msg=err, exc_info=True)
        finally:
            logging.info(f'Returning data from request: {self.url.constituencies_url()}, with params: {params}')
            return response

    #Returns the contents of the parties data from the API endpoint
    def fetch_parties_data(self, params: dict) -> dict:
        #Assinged the response variable before entering the try/except loop
        response = None

        logging.info(msg=logging.debug(msg=f'Fetching response from parties endpoint with params: {params}'))
        try:
            response = self.fetch_parties_response(params)
            response = response.json()
            logging.debug(msg=f'Response from {self.url.parties_url()} was: {response}')
        except Exception as err:
            logging.error(msg=err, exc_info=True)
        finally:
            logging.info(f'Returning data from request: {self.url.parties_url()}, with params: {params}')
            return response