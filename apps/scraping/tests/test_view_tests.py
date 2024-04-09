from django.test import TestCase, Client, RequestFactory
from django.urls import reverse


class ScrapingViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

    def test_get_request_returns_index_template(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    # def test_post_with_valid_credentials(self):
    #     response = self.client.post(reverse('scrap'), {'username': 'abacotestscraping ', 'password': 'TEst1234$'})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'results.html')