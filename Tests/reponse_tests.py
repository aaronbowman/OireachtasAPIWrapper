import unittest
import vcr

from Wrapper import fetch_data


class TestFetchData(unittest.TestCase):

    @vcr.use_cassette('fixtures/cassettes/legislation.yaml', record_mode='new_episodes')
    def test_fetch_legislation_response(self):
        test_case = (fetch_data.FetchResponse().fetch_legislation_response(params={}))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/debate.yaml', record_mode='new_episodes')
    def test_fetch_debate_response(self):
        test_case = (fetch_data.FetchResponse().fetch_debate_response(params={}))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/constituencies.yaml', record_mode='new_episodes')
    def test_fetch_constituencies_response(self):
        test_case = (fetch_data.FetchResponse().fetch_constituencies_response(params={}))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/parties.yaml', record_mode='new_episodes')
    def test_fetch_parties_response(self):
        test_case = (fetch_data.FetchResponse().fetch_parties_response(params={}))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/divisions.yaml', record_mode='new_episodes')
    def test_fetch_divisions_response(self):
        test_case = (fetch_data.FetchResponse().fetch_divisions_response(params={}))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/questions.yaml', record_mode='new_episodes')
    def test_fetch_questions_response(self):
        test_case = (fetch_data.FetchResponse().fetch_questions_response(params={}))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/houses.yaml', record_mode='new_episodes')
    def test_fetch_houses_response(self):
        test_case = (fetch_data.FetchResponse().fetch_houses_response(params={}))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/members.yaml', record_mode='new_episodes')
    def test_fetch_members_response(self):
        test_case = (fetch_data.FetchResponse().fetch_members_response(params={}))
        self.assertEqual(test_case.status_code, 200)