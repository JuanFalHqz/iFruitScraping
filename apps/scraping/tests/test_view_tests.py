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

# Reemplaza ".driver_view" con la ruta a tu módulo


# class TestScraping(TestCase):
#     def setUp(self):
#         pass
#
#     def eeee(self):
#         wishlist_elements = [
#             {
#                 'title': 'Minecraft - Volume Alpha',
#                 'artist': 'by C418',
#                 'tags': ['electronic', 'ambient', 'electro', 'electronica', 'idm', 'minecraft', 'ost', 'soundtrack',
#                          'video game', 'video game soundtrack', 'Texas']
#             },
#             {
#                 'title': 'ZYZZ',
#                 'artist': 'by baehyuni',
#                 'tags': ['alternative', 'hip-hop', 'hip-hop/rap', 'rap', 'alternative hip-hop', 'alternative pop',
#                          'indie', 'indie pop', 'jazz hop', 'pop', 'rock', 'South Korea']
#             },
#             {
#                 'title': 'Old Saltwater Passages',
#                 'artist': "by Serpent's Isle",
#                 'tags': ['ambient', 'black ambient', 'dark ambient', 'dungeon synth', 'fantasy synth',
#                          'old school dungeon synth', 'raw dungeon synth', 'sea synth', 'soundscape', 'United States']
#             }]
#
#         f = {'genres': ['classical', 'country', 'latin', 'pop', 'reggae'],
#              'artists': ['Black Flamingos', 'Slowey and The Boats', 'The Men In Gray Suits', 'The Surfrajettes',
#                          'The Primitive Finks', 'Lulufin The Woo Hoo', "The Swingin' Palms", 'The Sonoras',
#                          'Greg Townson', 'The Delstroyers', 'Los Frenéticos', 'Televisionaries', 'Bloodshot Bill',
#                          'The Hula Girls', 'The Hilo Hi-Flyers', 'Trevor Lake', 'The Manakooras', "Satan's Pilgrims",
#                          'GOONS!', 'Spike Marble', 'Stereophonic Space Sound Unlimited', 'Charlie Halloran',
#                          'The Babalooneys', "Shorty's Swingin Coconuts", 'The Jazztronauts', 'Messer Chups',
#                          'Frankie and the Pool Boys', 'The Tailspins', 'The McCharmlys', 'Ichi-Bons', 'Beachcombers',
#                          'The Charities', 'Los Baby Jaguars', 'Lulada Club', 'Aedi Records', 'Aether Mechanics',
#                          'Hypnus Records', 'Kabalion Records', 'Tome'],
#              'tags': ['hip-hop', 'hip-hop/rap', 'pop', 'rap', 'Detroit']
#              }
