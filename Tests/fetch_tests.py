import unittest


from Wrapper import fetch_data

class TestFetchData(unittest.TestCase):

    def test_fetch_legislation_data_response(self):
        test_case = (fetch_data.FetchResponse().fetch_legislation_response())
        self.assertEqual(test_case.status_code, 200)

    def test_fetch_debate_data_response(self):
        test_case = (fetch_data.FetchResponse().fetch_debate_response())
        self.assertEqual(test_case.status_code, 200)

    def test_fetch_constituencies_data_response(self):
        test_case = (fetch_data.FetchResponse().fetch_constituencies_response())
        self.assertEqual(test_case.status_code, 200)

    def test_fetch_parties_data_response(self):
        test_case = (fetch_data.FetchResponse().fetch_parties_response())
        self.assertEqual(test_case.status_code, 200)

    def test_fetch_divisions_data_response(self):
        test_case = (fetch_data.FetchResponse().fetch_divisions_response())
        self.assertEqual(test_case.status_code, 200)

    def test_fetch_questions_data_response(self):
        test_case = (fetch_data.FetchResponse().fetch_questions_response())
        self.assertEqual(test_case.status_code, 200)

    def test_fetch_houses_data_response(self):
        test_case = (fetch_data.FetchResponse().fetch_houses_response())
        self.assertEqual(test_case.status_code, 200)

    def test_fetch_members_data_response(self):
        test_case = (fetch_data.FetchResponse().fetch_members_response())
        self.assertEqual(test_case.status_code, 200)