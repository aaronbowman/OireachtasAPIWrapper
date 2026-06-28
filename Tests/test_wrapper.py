<<<<<<< HEAD
import os
from unittest import TestCase

import vcr
=======
import pytest
from unittest.mock import Mock
>>>>>>> df46be9a75c229a86acd3777c1f54d19c556bc78

from OireachtasAPI import wrapper

CASSETTES = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures', 'cassettes')


@pytest.mark.parametrize(
    ("endpoint_name", "expected_url"),
    [
        ("legislation", "https://api.oireachtas.ie/v1/legislation"),
        ("debates", "https://api.oireachtas.ie/v1/debates"),
        ("constituencies", "https://api.oireachtas.ie/v1/constituencies"),
        ("parties", "https://api.oireachtas.ie/v1/parties"),
        ("divisions", "https://api.oireachtas.ie/v1/divisions"),
        ("questions", "https://api.oireachtas.ie/v1/questions"),
        ("houses", "https://api.oireachtas.ie/v1/houses"),
        ("members", "https://api.oireachtas.ie/v1/members"),
    ],
)
def test_fetch_endpoint_returns_expected_url(endpoint_name, expected_url):
    assert wrapper.Wrapper()._fetch_endpoint(endpoint_name=endpoint_name) == expected_url


def test_wrapper_make_request_uses_api_client(monkeypatch, response_factory):
    payload = {"head": {"counts": {"billCount": 1}}}
    mock_response = response_factory(status_code=200, json_data=payload)
    mock_make_request = Mock(return_value=mock_response)
    monkeypatch.setattr(wrapper.Wrapper, "make_request", mock_make_request)

    response = wrapper.Wrapper().wrapper_make_request(endpoint_name="legislation", params={"limit": 1})

<<<<<<< HEAD
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

    def test__fetch_endpoint_unknown_raises(self):
        with self.assertRaises(ValueError):
            wrapper.Wrapper()._fetch_endpoint(endpoint_name='nonexistent')

    @vcr.use_cassette(os.path.join(CASSETTES, 'legislation.yaml'), record_mode='none')
    def test_wrapper_make_legislation_request(self):
        test_case = wrapper.Wrapper().wrapper_make_request(endpoint_name='legislation', params={'limit': 1})
        test_case = test_case.json()
        self.assertIn('billCount', test_case['head']['counts'])

    @vcr.use_cassette(os.path.join(CASSETTES, 'questions.yaml'), record_mode='none')
    def test_wrapper_make_question_request(self):
        test_case = wrapper.Wrapper().wrapper_make_request(endpoint_name='questions', params={'limit': 1})
        test_case = test_case.json()
        self.assertIn('questionCount', test_case['head']['counts'])

    @vcr.use_cassette(os.path.join(CASSETTES, 'debates.yaml'), record_mode='none')
    def test_wrapper_make_debate_request(self):
        test_case = wrapper.Wrapper().wrapper_make_request(endpoint_name='debates', params={'limit': 1})
        test_case = test_case.json()
        self.assertIn('debateCount', test_case['head']['counts'])

    @vcr.use_cassette(os.path.join(CASSETTES, 'constituencies.yaml'), record_mode='none')
    def test_wrapper_make_constituencies_request(self):
        test_case = wrapper.Wrapper().wrapper_make_request(endpoint_name='constituencies', params={'limit': 1})
        test_case = test_case.json()
        self.assertIn('constituencyCount', test_case['head']['counts'])

    @vcr.use_cassette(os.path.join(CASSETTES, 'parties.yaml'), record_mode='none')
    def test_wrapper_make_parties_request(self):
        test_case = wrapper.Wrapper().wrapper_make_request(endpoint_name='parties', params={'limit': 1})
        test_case = test_case.json()
        self.assertIn('partyCount', test_case['head']['counts'])

    @vcr.use_cassette(os.path.join(CASSETTES, 'divisions.yaml'), record_mode='none')
    def test_wrapper_make_divisions_request(self):
        test_case = wrapper.Wrapper().wrapper_make_request(endpoint_name='divisions')
        self.assertEqual(test_case.status_code, 200)
=======
    assert response.json()["head"]["counts"]["billCount"] == 1
    mock_make_request.assert_called_once_with(
        endpoint="https://api.oireachtas.ie/v1/legislation", params={"limit": 1}
    )
>>>>>>> df46be9a75c229a86acd3777c1f54d19c556bc78
