import os
import unittest

import vcr

from OireachtasAPI import api

CASSETTES = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures', 'cassettes')


class TestAPI(unittest.TestCase):

    @vcr.use_cassette(os.path.join(CASSETTES, 'legislation.yaml'), record_mode='none')
    def test_legislation_endpoint(self):
        test_case = (api.API().make_request(endpoint='https://api.oireachtas.ie/v1/legislation'))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette(os.path.join(CASSETTES, 'debates.yaml'), record_mode='none')
    def test_debates_endpoint(self):
        test_case = (api.API().make_request(endpoint='https://api.oireachtas.ie/v1/debates'))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette(os.path.join(CASSETTES, 'constituencies.yaml'), record_mode='none')
    def test_constituencies_endpoint(self):
        test_case = (api.API().make_request(endpoint='https://api.oireachtas.ie/v1/constituencies'))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette(os.path.join(CASSETTES, 'parties.yaml'), record_mode='none')
    def test_parties_endpoint(self):
        test_case = (api.API().make_request(endpoint='https://api.oireachtas.ie/v1/parties'))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette(os.path.join(CASSETTES, 'divisions.yaml'), record_mode='none')
    def test_divisions_endpoint(self):
        test_case = (api.API().make_request(endpoint='https://api.oireachtas.ie/v1/divisions'))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette(os.path.join(CASSETTES, 'questions.yaml'), record_mode='none')
    def test_questions_endpoint(self):
        test_case = (api.API().make_request(endpoint='https://api.oireachtas.ie/v1/questions'))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette(os.path.join(CASSETTES, 'houses.yaml'), record_mode='none')
    def test_houses_endpoint(self):
        test_case = (api.API().make_request(endpoint='https://api.oireachtas.ie/v1/houses'))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette(os.path.join(CASSETTES, 'members.yaml'), record_mode='none')
    def test_members_endpoint(self):
        test_case = (api.API().make_request(endpoint='https://api.oireachtas.ie/v1/members'))
        self.assertEqual(test_case.status_code, 200)
