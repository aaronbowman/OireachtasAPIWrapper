import unittest
import vcr

from Wrapper import fetch_data


class FetchDataTests(unittest.TestCase):

    @vcr.use_cassette('fixtures/cassettes/legislation.yaml', record_mode='new_episodes')
    def test_fetch_legislation_data_response(self):
        test_case = fetch_data.FetchData().fetch_legislation_data(params={'limit' : 1})
        self.assertIn('billCount', test_case['head']['counts'])

    @vcr.use_cassette('fixtures/cassettes/questions.yaml', record_mode='new_episodes')
    def test_fetch_questions_data_response(self):
        test_case = fetch_data.FetchData().fetch_questions_data(params={'limit' : 1})
        self.assertIn('questionCount', test_case['head']['counts'])

    @vcr.use_cassette('fixtures/cassettes/debate.yaml', record_mode='new_episodes')
    def test_fetch_debate_data_response(self):
        test_case = fetch_data.FetchData().fetch_debate_data(params={'limit' : 1})
        self.assertIn('debateCount', test_case['head']['counts'])

    @vcr.use_cassette('fixtures/cassettes/constituencies.yaml', record_mode='new_episodes')
    def test_fetch_constituencies_data_response(self):
        test_case = fetch_data.FetchData().fetch_constituencies_data(params={})
        self.assertIn('constituencyCount', test_case['head']['counts'])

    @vcr.use_cassette('fixtures/cassettes/parties.yaml', record_mode='new_episodes')
    def test_fetch_parties_data_response(self):
        test_case = fetch_data.FetchData().fetch_parties_data(params={})
        self.assertIn('partyCount', test_case['head']['counts'])