import unittest

from Wrapper import urls

class TestURL(unittest.TestCase):

    def test_legislation_url(self):
        test_url = urls.URLs().legislation_url()
        self.assertEqual(test_url, 'https://api.oireachtas.ie/v1/legislation')

    def test_debate_url(self):
        test_url = urls.URLs().debate_url()
        self.assertEqual(test_url, 'https://api.oireachtas.ie/v1/debates')

    def test_constituencies_url(self):
        test_url = urls.URLs().constituencies_url()
        self.assertEqual(test_url, 'https://api.oireachtas.ie/v1/constituencies')

    def test_parties_url(self):
        test_url = urls.URLs().parties_url()
        self.assertEqual(test_url, 'https://api.oireachtas.ie/v1/parties')

    def test_divisions_url(self):
        test_url = urls.URLs().divisions_url()
        self.assertEqual(test_url, 'https://api.oireachtas.ie/v1/divisions')

    def test_questions_url(self):
        test_url = urls.URLs().questions_url()
        self.assertEqual(test_url, 'https://api.oireachtas.ie/v1/questions')

    def test_houses_url(self):
        test_url = urls.URLs().houses_url()
        self.assertEqual(test_url, 'https://api.oireachtas.ie/v1/houses')

    def test_members_url(self):
        test_url = urls.URLs().members_url()
        self.assertEqual(test_url, 'https://api.oireachtas.ie/v1/members')