import unittest
import vcr
import logging

from Wrapper import fetch_data

formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='TestLogger.log', level=logging.DEBUG, format=formatter)

class TestFetchData(unittest.TestCase):

    @vcr.use_cassette('fixtures/cassettes/legislation.yaml')
    def test_fetch_legislation_response(self):
        test_case = (fetch_data.FetchResponse().fetch_legislation_response(params={}))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/debate.yaml')
    def test_fetch_debate_response(self):
        test_case = (fetch_data.FetchResponse().fetch_debate_response(params={}))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/constituencies.yaml')
    def test_fetch_constituencies_response(self):
        test_case = (fetch_data.FetchResponse().fetch_constituencies_response(params={}))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/parties.yaml')
    def test_fetch_parties_response(self):
        test_case = (fetch_data.FetchResponse().fetch_parties_response(params={}))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/divisions.yaml')
    def test_fetch_divisions_response(self):
        test_case = (fetch_data.FetchResponse().fetch_divisions_response(params={}))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/questions.yaml')
    def test_fetch_questions_response(self):
        test_case = (fetch_data.FetchResponse().fetch_questions_response(params={}))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/houses.yaml')
    def test_fetch_houses_response(self):
        test_case = (fetch_data.FetchResponse().fetch_houses_response(params={}))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/members.yaml')
    def test_fetch_members_response(self):
        test_case = (fetch_data.FetchResponse().fetch_members_response(params={}))
        self.assertEqual(test_case.status_code, 200)