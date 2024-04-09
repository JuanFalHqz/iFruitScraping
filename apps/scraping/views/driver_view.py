from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from webdriver_manager.chrome import ChromeDriverManager


class DriverView:
    """
    Clase encargada de configurar algunos parámetros del driver web.
    """

    __driver = None

    def load_driver(self):
        """
        Inicializa el controlador de Selenium con los parámetros necesarios.

        """
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-extensions")
        # options.add_argument("--incognito")
        options.add_argument("--window-size=1280,1000")
        service = ChromiumService(executable_path=ChromeDriverManager().install())
        self.__driver = webdriver.Chrome(service=service, options=options)

    def get_driver(self):
        """
        Retorna el controlador de Selenium.

        :return: El controlador de Selenium
        """
        return self.__driver

    def quit_driver(self):
        """
        Cierra y finaliza el controlador de Selenium.

        """
        self.__driver.quit()
        self.__driver = None
