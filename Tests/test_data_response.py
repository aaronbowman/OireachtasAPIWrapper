<<<<<<< HEAD
import os
import unittest

import vcr
=======
import pytest
from unittest.mock import Mock
>>>>>>> df46be9a75c229a86acd3777c1f54d19c556bc78

from OireachtasAPI import api

CASSETTES = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures', 'cassettes')


@pytest.mark.parametrize(
    ("endpoint", "count_key"),
    [
        ("https://api.oireachtas.ie/v1/legislation", "billCount"),
        ("https://api.oireachtas.ie/v1/questions", "questionCount"),
        ("https://api.oireachtas.ie/v1/debates", "debateCount"),
        ("https://api.oireachtas.ie/v1/constituencies", "constituencyCount"),
        ("https://api.oireachtas.ie/v1/parties", "partyCount"),
    ],
)
def test_fetch_data_response_contains_expected_counts(monkeypatch, response_factory, endpoint, count_key):
    payload = {"head": {"counts": {count_key: 1}}}
    mock_response = response_factory(status_code=200, json_data=payload)
    mock_get = Mock(return_value=mock_response)
    monkeypatch.setattr(api.requests, "get", mock_get)

<<<<<<< HEAD
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
=======
    response = api.API().make_request(endpoint=endpoint, params={"limit": 1})

    assert count_key in response.json()["head"]["counts"]
    mock_get.assert_called_once_with(url=endpoint, params={"limit": 1})
>>>>>>> df46be9a75c229a86acd3777c1f54d19c556bc78
