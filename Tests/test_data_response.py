import os
import unittest

import vcr

from OireachtasAPI import api

CASSETTES = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures', 'cassettes')


class FetchDataTests(unittest.TestCase):

    @vcr.use_cassette(os.path.join(CASSETTES, 'legislation.yaml'), record_mode='none')
    def test_fetch_legislation_data_response(self):
        test_case = api.API().make_request(endpoint='https://api.oireachtas.ie/v1/legislation', params={'limit': 1})
        test_case = test_case.json()
        self.assertIn('billCount', test_case['head']['counts'])

    @vcr.use_cassette(os.path.join(CASSETTES, 'questions.yaml'), record_mode='none')
    def test_fetch_questions_data_response(self):
        test_case = api.API().make_request(endpoint='https://api.oireachtas.ie/v1/questions', params={'limit': 1})
        test_case = test_case.json()
        self.assertIn('questionCount', test_case['head']['counts'])

    @vcr.use_cassette(os.path.join(CASSETTES, 'debates.yaml'), record_mode='none')
    def test_fetch_debate_data_response(self):
        test_case = api.API().make_request(endpoint='https://api.oireachtas.ie/v1/debates', params={'limit': 1})
        test_case = test_case.json()
        self.assertIn('debateCount', test_case['head']['counts'])

    @vcr.use_cassette(os.path.join(CASSETTES, 'constituencies.yaml'), record_mode='none')
    def test_fetch_constituencies_data_response(self):
        test_case = api.API().make_request(endpoint='https://api.oireachtas.ie/v1/constituencies', params={'limit': 1})
        test_case = test_case.json()
        self.assertIn('constituencyCount', test_case['head']['counts'])

    @vcr.use_cassette(os.path.join(CASSETTES, 'parties.yaml'), record_mode='none')
    def test_fetch_parties_data_response(self):
        test_case = api.API().make_request(endpoint='https://api.oireachtas.ie/v1/parties', params={'limit': 1})
        test_case = test_case.json()
        self.assertIn('partyCount', test_case['head']['counts'])
