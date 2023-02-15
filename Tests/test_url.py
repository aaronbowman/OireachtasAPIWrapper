import unittest

from OireachtasAPI import urls


class TestURL(unittest.TestCase):


    def test__legislation_url(self):
        test_url = urls.URLs()._legislation_url()
        self.assertEqual(test_url, 'https://api.oireachtas.ie/v1/legislation')

    def test__debate_url(self):
        test_url = urls.URLs()._debates_url()
        self.assertEqual(test_url, 'https://api.oireachtas.ie/v1/debates')

    def test__constituencies_url(self):
        test_url = urls.URLs()._constituencies_url()
        self.assertEqual(test_url, 'https://api.oireachtas.ie/v1/constituencies')

    def test__parties_url(self):
        test_url = urls.URLs()._parties_url()
        self.assertEqual(test_url, 'https://api.oireachtas.ie/v1/parties')

    def test__divisions_url(self):
        test_url = urls.URLs()._divisions_url()
        self.assertEqual(test_url, 'https://api.oireachtas.ie/v1/divisions')

    def test__questions_url(self):
        test_url = urls.URLs()._questions_url()
        self.assertEqual(test_url, 'https://api.oireachtas.ie/v1/questions')

    def test__houses_url(self):
        test_url = urls.URLs()._houses_url()
        self.assertEqual(test_url, 'https://api.oireachtas.ie/v1/houses')

    def test__members_url(self):
        test_url = urls.URLs()._members_url()
        self.assertEqual(test_url, 'https://api.oireachtas.ie/v1/members')