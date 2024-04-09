from apps.scraping.views.driver_view import DriverView
from django.test import TestCase
from selenium.webdriver.chrome.webdriver import WebDriver


# class DriverViewTestCase(TestCase):
#     def setUp(self):
#         self.driver_view = DriverView()
#
#     def test_load_driver(self):
#         self.assertIsNone(self.driver_view.get_driver())  # Asegurarse de que el driver sea None antes de cargarlo
#         self.driver_view.load_driver()
#         self.assertIsInstance(self.driver_view.get_driver(),
#                               WebDriver)  # Asegurarse de que se haya cargado un driver de Selenium
#         self.driver_view.quit_driver()
#
#     def test_get_driver(self):
#         self.assertIsNone(self.driver_view.get_driver())  # Asegurarse de que el driver sea None inicialmente
#         self.driver_view.load_driver()
#         self.assertIsInstance(self.driver_view.get_driver(),
#                               WebDriver)  # Asegurarse de que se haya obtenido un driver de Selenium
#         self.assertIsNotNone(
#             self.driver_view.get_driver())  # Asegurarse de que el driver no sea None después de obtenerlo
#         self.driver_view.quit_driver()
#
#     def test_quit_driver(self):
#         self.driver_view.load_driver()  # Cargar el driver primero
#         self.assertIsNotNone(self.driver_view.get_driver())  # Asegurarse de que el driver no sea None antes de cerrarlo
#         self.driver_view.quit_driver()
#         self.assertIsNone(self.driver_view.get_driver())  # Asegurarse de que el driver sea None después de cerrarlo
