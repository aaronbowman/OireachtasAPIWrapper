from unittest import TestCase

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