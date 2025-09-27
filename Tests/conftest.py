from unittest.mock import Mock

import pytest


@pytest.fixture
def response_factory():
    """Factory for creating mock response objects with configurable JSON payloads."""

    def factory(*, status_code=200, json_data=None):
        mock_response = Mock()
        mock_response.status_code = status_code
        mock_response.json.return_value = json_data or {}
        return mock_response

    return factory
