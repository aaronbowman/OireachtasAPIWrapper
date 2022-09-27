import unittest

import vcr

from Wrapper import api


class TestAPI(unittest.TestCase):

    @vcr.use_cassette('fixtures/cassettes/legislation.yaml', record_mode='new_episodes')
    def test_legislation_endpoint(self):
        test_case = (api.API().make_request(endpoint='https://api.oireachtas.ie/v1/legislation'))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/debates.yaml', record_mode='new_episodes')
    def test_debates_endpoint(self):
        test_case = (api.API().make_request(endpoint='https://api.oireachtas.ie/v1/debates'))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/constituencies.yaml', record_mode='new_episodes')
    def test_constituencies_endpoint(self):
        test_case = (api.API().make_request(endpoint='https://api.oireachtas.ie/v1/constituencies'))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/parties.yaml', record_mode='new_episodes')
    def test_parties_endpoint(self):
        test_case = (api.API().make_request(endpoint='https://api.oireachtas.ie/v1/parties'))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/divisions.yaml', record_mode='new_episodes')
    def test_divisions_endpoint(self):
        test_case = (api.API().make_request(endpoint='https://api.oireachtas.ie/v1/divisions'))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/questions.yaml', record_mode='new_episodes')
    def test_questions_endpoint(self):
        test_case = (api.API().make_request(endpoint='https://api.oireachtas.ie/v1/questions'))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/houses.yaml', record_mode='new_episodes')
    def test_houses_endpoint(self):
        test_case = (api.API().make_request(endpoint='https://api.oireachtas.ie/v1/houses'))
        self.assertEqual(test_case.status_code, 200)

    @vcr.use_cassette('fixtures/cassettes/members.yaml', record_mode='new_episodes')
    def test_members_endpoint(self):
        test_case = (api.API().make_request(endpoint='https://api.oireachtas.ie/v1/members'))
        self.assertEqual(test_case.status_code, 200)



