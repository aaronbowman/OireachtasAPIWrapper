import unittest
import vcr
import logging

from Wrapper import fetch_data

formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='TestLogger.log', level=logging.DEBUG, format=formatter)

class FetchDataTests(unittest.TestCase):

    @vcr.use_cassette('fixtures/cassettes/legislation.yaml')
    def test_fetch_legislation_data_response(self):
        test_case = fetch_data.FetchData().fetch_legislation_data(params={'limit' : 1})
        self.assertIn('billCount', test_case['head']['counts'])

    @vcr.use_cassette('fixtures/cassettes/questions.yaml')
    def test_fetch_questions_data_response(self):
        test_case = fetch_data.FetchData().fetch_questions_data(params={'limit' : 1})
        print(test_case)
        self.assertIn('questionCount', test_case['head']['counts'])

    @vcr.use_cassette('fixtures/cassettes/debate.yaml')
    def test_fetch_questions_data_response(self):
        test_case = fetch_data.FetchData().fetch_debate_data(params={'limit' : 1})
        print(test_case)
        self.assertIn('questionCount', test_case['head']['counts'])
