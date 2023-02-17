from unittest import TestCase

import vcr

from OireachtasAPI import wrapper


class TestWrapper(TestCase):

    def test__fetch_endpoint_legislation(self):
        test_case = wrapper.Wrapper()._fetch_endpoint(endpoint_name='legislation')
        self.assertEqual(test_case, 'https://api.oireachtas.ie/v1/legislation')

    def test__fetch_endpoint_debates(self):
        test_case = wrapper.Wrapper()._fetch_endpoint(endpoint_name='debates')
        self.assertEqual(test_case, 'https://api.oireachtas.ie/v1/debates')

    def test__fetch_endpoint_constituencies(self):
        test_case = wrapper.Wrapper()._fetch_endpoint(endpoint_name='constituencies')
        self.assertEqual(test_case, 'https://api.oireachtas.ie/v1/constituencies')

    def test__fetch_endpoint_parties(self):
        test_case = wrapper.Wrapper()._fetch_endpoint(endpoint_name='parties')
        self.assertEqual(test_case, 'https://api.oireachtas.ie/v1/parties')

    def test__fetch_endpoint_divisions(self):
        test_case = wrapper.Wrapper()._fetch_endpoint(endpoint_name='divisions')
        self.assertEqual(test_case, 'https://api.oireachtas.ie/v1/divisions')

    def test__fetch_endpoint_questions(self):
        test_case = wrapper.Wrapper()._fetch_endpoint(endpoint_name='questions')
        self.assertEqual(test_case, 'https://api.oireachtas.ie/v1/questions')

    def test__fetch_endpoint_houses(self):
        test_case = wrapper.Wrapper()._fetch_endpoint(endpoint_name='houses')
        self.assertEqual(test_case, 'https://api.oireachtas.ie/v1/houses')

    def test__fetch_endpoint_members(self):
        test_case = wrapper.Wrapper()._fetch_endpoint(endpoint_name='members')
        self.assertEqual(test_case, 'https://api.oireachtas.ie/v1/members')

    #Testing that the wrapper actually returns the same info as the API make request fuction
    @vcr.use_cassette('fixtures/cassettes/legislation.yaml', record_mode='new_episodes')
    def test_wrapper_make_legislation_request(self):
        test_case = wrapper.Wrapper().wrapper_make_request(endpoint_name='legislation', params={'limit':1})
        test_case = test_case.json()
        self.assertIn('billCount', test_case['head']['counts'])

    @vcr.use_cassette('fixtures/cassettes/questions.yaml', record_mode='new_episodes')
    def test_wrapper_make_question_request(self):
        test_case = wrapper.Wrapper().wrapper_make_request(endpoint_name='questions', params={'limit':1})
        test_case = test_case.json()
        self.assertIn('questionCount', test_case['head']['counts'])

    @vcr.use_cassette('fixtures/cassettes/debates.yaml', record_mode='new_episodes')
    def test_wrapper_make_debate_request(self):
        test_case = wrapper.Wrapper().wrapper_make_request(endpoint_name='debates', params={'limit':1})
        test_case = test_case.json()
        self.assertIn('debateCount', test_case['head']['counts'])

    @vcr.use_cassette('fixtures/cassettes/constituencies.yaml', record_mode='new_episodes')
    def test_wrapper_make_constituencies_request(self):
        test_case = wrapper.Wrapper().wrapper_make_request(endpoint_name='constituencies', params={'limit':1})
        test_case = test_case.json()
        self.assertIn('constituencyCount', test_case['head']['counts'])

    @vcr.use_cassette('fixtures/cassettes/parties.yaml', record_mode='new_episodes')
    def test_wrapper_make_parties_request(self):
        test_case = wrapper.Wrapper().wrapper_make_request(endpoint_name='parties', params={'limit':1})
        test_case = test_case.json()
        self.assertIn('partyCount', test_case['head']['counts'])