<<<<<<< HEAD
import os
import unittest
=======
import pytest
from unittest.mock import Mock
>>>>>>> df46be9a75c229a86acd3777c1f54d19c556bc78

from OireachtasAPI import api, errors

CASSETTES = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures', 'cassettes')


@pytest.mark.parametrize(
    "endpoint",
    [
        "https://api.oireachtas.ie/v1/legislation",
        "https://api.oireachtas.ie/v1/debates",
        "https://api.oireachtas.ie/v1/constituencies",
        "https://api.oireachtas.ie/v1/parties",
        "https://api.oireachtas.ie/v1/divisions",
        "https://api.oireachtas.ie/v1/questions",
        "https://api.oireachtas.ie/v1/houses",
        "https://api.oireachtas.ie/v1/members",
    ],
)
def test_make_request_success(monkeypatch, response_factory, endpoint):
    mock_response = response_factory(status_code=200)
    mock_get = Mock(return_value=mock_response)
    monkeypatch.setattr(api.requests, "get", mock_get)

<<<<<<< HEAD
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
=======
    response = api.API().make_request(endpoint=endpoint)

    assert response.status_code == 200
    mock_get.assert_called_once_with(url=endpoint, params={})


@pytest.mark.parametrize(
    ("status_code", "expected_exception"),
    [
        (400, errors.BadRequest),
        (401, errors.Unauthorised),
        (403, errors.Forbidden),
        (404, errors.NotFound),
        (429, errors.TooManyRequests),
    ],
)
def test_make_request_raises_for_error_status(monkeypatch, response_factory, status_code, expected_exception):
    mock_response = response_factory(status_code=status_code)
    mock_get = Mock(return_value=mock_response)
    monkeypatch.setattr(api.requests, "get", mock_get)

    with pytest.raises(expected_exception):
        api.API().make_request(endpoint="https://api.oireachtas.ie/v1/legislation")

    mock_get.assert_called_once()
>>>>>>> df46be9a75c229a86acd3777c1f54d19c556bc78
