import random
import time
from abc import abstractmethod

from selenium.common import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from apps.scraping.views.driver_view import DriverView


# Create your views here.
class AbstractScrapingClass:
    def login(user, password):
        pass

    def process(self):
        pass


class Scraper(AbstractScrapingClass):
    """
    Clase encargada de realizar la recogida de datos del sitio web

    :var : driver_view: DriverView() - Instancia de la clase DriverView, que se encarga de realizar las operaciones como la configuración del driver

    :var : driver: WebDriver() - contiene el driver con el cual se controlará el navegador web
    """
    driver_view = None
    driver = None

    def __init__(self):
        self.driver_view = DriverView()
        self.driver_view.load_driver()
        self.driver = self.driver_view.get_driver()

    def login(self, user, password):
        """
        Función encargada de hacer el inicio de sesión en el sitio.

        :param user: string - usuario
        :param password: string - contraseña
        :return: None
        :raise: Exception - En caso de encontrar algún error
        """
        try:
            user_input = self.driver.find_element(By.ID, 'username-field')
            WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of(user_input))
            user_input.send_keys(user)
            time.sleep(5)

            pass_inputs = self.driver.find_elements(By.ID, 'password-field')
            if pass_inputs:
                print('Encontrado por id')
                pass_input = pass_inputs[0]  # Tomar el primer elemento de la lista
                pass_input.send_keys(password)
                time.sleep(4)
            else:
                pass_inputs = self.driver.find_elements(By.XPATH, '//*[@id="password-field"]')
                if pass_inputs:
                    print('Encontrado por XPATH')
                    pass_input = pass_inputs[0]  # Tomar el primer elemento de la lista
                    pass_input.send_keys(password)
                    time.sleep(3)
                else:
                    pass_inputs = self.driver.find_elements(By.XPATH,
                                                            '/html/body/div[4]/div/div[2]/div[1]/div/div/form/div[1]/div[2]/div/input')
                    if pass_inputs:
                        print('Encontrado por XPATH Completo')
                        pass_input = pass_inputs[0]  # Tomar el primer elemento de la lista
                        pass_input.send_keys(password)
                        time.sleep(3)
            if not pass_inputs:
                try:
                    pass_input = self.driver.find_elements(By.XPATH, '//*[@id="password-field"]')
                    WebDriverWait(self.driver, 2).until(
                        expected_conditions.presence_of_element_located(By.XPATH, '//*[@id="password-field"]'))
                    print('Encontrado por XPATH dada una exepción')
                    pass_input.send_keys(password)
                    time.sleep(2)
                except TimeoutException:
                    pass_input = self.driver.find_elements(By.XPATH,
                                                           '/html/body/div[4]/div/div[2]/div[1]/div/div/form/div[1]/div[2]/div/input')
                    WebDriverWait(self.driver, 2).until(expected_conditions.presence_of_element_located(By.XPATH,
                                                                                                        '/html/body/div[4]/div/div[2]/div[1]/div/div/form/div[1]/div[2]/div/input'))
                    print('Encontrado por XPATH Completo dada una exepción')
                    pass_input.send_keys(password)
                    time.sleep(2)
            if pass_inputs:
                button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
                WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of(button))
                time.sleep(3)
                button.click()
            time.sleep(3)
            pass_input_rectification = self.driver.find_elements(By.ID, 'password-field')
            if pass_input_rectification:
                self.driver_view.quit_driver()
                raise Exception(
                    'No ha iniciado sesión el usuario con las credenciales proporcionadas. \n Por favor revise que el '
                    'usuario exista. En caso de que las credenciales del usuario estén correctas puede que haya un '
                    'CAPTCHAT.')
        except Exception as e:
            raise Exception(e.__str__())

    def process(self):
        """
        Se encarga de realizar el proceso de recogida de datos

        :return: {} - Diccionario con los resultados de obtener los datos de la lista de deseos, de lo que sigue y de la fiabilidad
        :raise: Exception - En caso de encontrar algún error
        """
        scraper_data = {}
        try:
            wishlist = self.get_wishlist_data()
            scraper_data['wishlist'] = wishlist
            following = self.get_following_data()
            scraper_data['following'] = following
            count_of_elements_with_tag_in_following_genres = self.get_count_of_elements_with_tag_in_following_genres(
                wishlist, following['genres'])
            scraper_data['reliability'] = self.get_reliability(count_of_elements_with_tag_in_following_genres,
                                                               len(wishlist))
        except Exception as e:
            raise Exception(e.__str__())
        return scraper_data

    def load_page(self, url):
        """
        Se encarga de abrir la url pasada por parámetro

        :param url: url a la cual se quiere acceder
        :return: None
        """
        # abre la url pasada por parámetro
        self.driver.get(url)

    def get_wishlist_data(self):
        """
        Busca y guarda los elementos que el usuario posee en su lista de deseos y los almacena en una lista
        Los elementos poseen el siguiente formato: {'title': '','artist': '','tags': []}. La lista a retornar posee el
        siguiente formato: [{'title': '','artist': '','tags': []},{'title': '','artist': '','tags': []}]

        :return: [] - Lista con los elementos en su lista de deseos
        :raise: Exception - En caso de encontrar algún error
        """
        try:
            wishlist_elements = []
            # 1 Coger los elementos con clase collection-title-details
            html_elements = self.driver.find_elements(By.CLASS_NAME, 'collection-title-details')
            # 2 Por cada elemento
            for element in html_elements:
                # 2.1 Coger el título del elemento que tiene clase collection-item-title
                title = element.find_element(By.CLASS_NAME, 'collection-item-title')
                WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of(title))
                title = title.text
                self.wait_long_time()
                # 2.2 Coger el artista que es un div collection-item-artist, guardarlo
                artist = element.find_element(By.CLASS_NAME, 'collection-item-artist')
                WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of(artist))
                artist = artist.text
                self.wait_long_time()
                # 2.3 Redirigir a la etiqueta <a> dentro
                element.click()
                # 2.3.1 Cambiar al índice de la nueva ventana
                ventanas = self.driver.window_handles
                self.driver.switch_to.window(ventanas[1])
                # 2.3.2 Tomar los datos de las etiquetas
                html_content = self.driver.find_element(By.CLASS_NAME, 'tralbumData.tralbum-tags.tralbum-tags-nu')
                WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of(html_content))
                self.wait_long_time()
                html_tags = html_content.find_elements(By.TAG_NAME, 'a')
                self.driver.implicitly_wait(5)
                self.wait_long_time()
                tags = []
                for tag in html_tags:
                    tags.append(tag.text)
                # 2.3.3 Cerrar la ventana actual
                self.driver.close()
                # 2.3.4 Cambiar al índice de la ventana principal
                self.driver.switch_to.window(ventanas[0])
                wishlist_elements.append({
                    'title': title,
                    'artist': artist,
                    'tags': tags
                })
        except Exception as e:
            self.driver_view.quit_driver()
            raise Exception("Error mientras se hacía el scraping en la lista de elementos deseados.\n" + e.__str__())

        return wishlist_elements

    def get_following_data(self):
        """
        Busca los géneros, artistas y etiquetas que el usuario sigue y los almacena en una lista
        El diccionario a retornar posee el siguiente formato
        following_elements = {'genres': [], 'artists': [],'tags': []}
        :return: {} - diccionario con los géneros, artistas y etiquetas que el usuario sigue
        :raise: Exception - En caso de encontrar algún error
        """
        following_elements = {}
        artists = []
        genres = []
        tags = []

        try:
            # Redirigir a la sección de following
            following_button = self.driver.find_element(By.XPATH, '//*[@id="grid-tabs"]/li[3]')
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of(following_button))
            if following_button:
                following_button.click()
            self.wait_short_time()
            # Obtener los elementos(artistas y etiquetas) following

            artist_and_labels = self.driver.find_elements(By.CLASS_NAME, 'fan-username')
            for element in artist_and_labels:
                element.send_keys(Keys.CONTROL + Keys.RETURN)
                self.driver.switch_to.window(self.driver.window_handles[1])

                artists = self.get_following_artists(artists)
                tags = self.get_following_tags(tags)

                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                self.wait_short_time()
            genres = self.get_following_genres()
        except Exception as e:
            self.driver_view.quit_driver()
            raise Exception(
                "Error mientras se hacía el scraping en los elementos seguidos por el usuario.\n" + e.__str__())
        following_elements = {
            'genres': genres,
            'artists': artists,
            'tags': tags,
        }
        return following_elements

    def get_following_genres(self):
        """
        Busca y guarda los géneros encontrados en los géneros seguidos

        :return: [] - Lista de géneros con los nuevos géneros añadidos
        :raise: Exception - En caso de encontrar algún error
        """
        genres = []
        try:
            generes_button = self.driver.find_element(By.CSS_SELECTOR, 'li[data-tab="following-genres"]')
            self.driver.implicitly_wait(5)
            if generes_button:
                generes_button.click()
                self.wait_short_time()
            self.scroll_down(8)
            genres_html = self.driver.find_elements(By.CLASS_NAME, 'genre-name')
            self.driver.implicitly_wait(3)

            for genre in genres_html:
                if genre.text not in genres:
                    genres.append(genre.text)
        except Exception:
            return genres
        return genres

    def get_following_artists(self, artist):
        """
        Busca y guarda los artistas encontrados en los artistas seguidos

        :param artist: [] - Lista de artistas que se ha encontrado hasta el momento
        :return: [] - Lista de artistas con los nuevos artistas añadidos
        :raise: Exception - En caso de encontrar algún error
        """
        # Hacer clic en el botón del navbar correspondiente a los artistas
        artist_button = None
        try:
            artist_button = self.driver.find_element(By.XPATH, '//a[@href="/artists"]')
            self.driver.implicitly_wait(3)
            if artist_button:
                artist_button.click()
                self.wait_short_time()
            # Recoger los artistas si existen
            artist_html = self.driver.find_elements(By.CLASS_NAME, 'artists-grid-name')
            self.driver.implicitly_wait(3)
            if artist_html:
                for element in artist_html:
                    if element.text not in artist:
                        artist.append(element.text)
            if artist_button:
                self.driver.back()
        except Exception:
            if artist_button:
                artist_button.click()
            return artist

        return artist

    def get_following_tags(self, tags):
        """
        Busca y guarda las etiquetas encontradas en las etiquetas seguidas

        :param tags: [] - Lista de etiquetas que se ha encontrado hasta el momento
        :return: [] - Lista de etiquetas con las nuevas etiquetas añadidas
        :raise: Exception - En caso de encontrar algún error
        """
        try:
            tags_html = self.driver.find_elements(By.CLASS_NAME, 'tag')
            self.driver.implicitly_wait(3)
            if tags_html:
                for tag in tags_html:
                    if tag.text not in tags:
                        tags.append(tag.text)
        except Exception:
            return tags
        return tags

    def get_reliability(self, count_of_elements_with_tag_in_following_genres, count_total_wishlist_elements):
        """
        Función que calcula la fiabilidad: Número de elementos en la wishlist con al menos una etiqueta de los que aparecen en el listado de géneros seguidos / Número de elementos totales

        :param count_of_elements_with_tag_in_following_genres: int - Número de elementos en la wishlist con al menos una etiqueta de los que aparecen en el listado de géneros seguidos.
        :param count_total_wishlist_elements: int - Número de elementos totales encontrados en la wishlist
        :return: float - valor de la fiabilidad
        """
        if count_total_wishlist_elements > 0:
            return count_of_elements_with_tag_in_following_genres / count_total_wishlist_elements
        return 0

    def get_count_of_elements_with_tag_in_following_genres(self, wishlist, genres_following):
        """
        Número de elementos en la wishlist con al menos una etiqueta de los que aparecen en el listado de géneros seguidos.

        :param wishlist: [] - lista de elementos que se encontraron en la wishlist
        :param genres_following: [] - lista de géneros encontrados en la following
        :return: int - Número de elementos
        """
        count_of_elements_with_tag_in_following_genres = 0
        for w in wishlist:
            tags = w['tags']
            for tag in tags:
                if tag in genres_following:
                    count_of_elements_with_tag_in_following_genres += 1
                    break

        return count_of_elements_with_tag_in_following_genres

    def wait_long_time(self):
        """
        Establece un tiempo aleatorio a esperar entre 5 a 10 segundos

        :return: int - Tiempo a esperar
        """
        time.sleep(random.randint(5, 10))

    def wait_short_time(self):
        """
        Establece un tiempo aleatorio a esperar entre 1 a 5 segundos

        :return: int - Tiempo a esperar
        """
        time.sleep(random.randint(1, 5))

    def scroll_down(self, speed=8):
        """
        Va al final de la página haciendo scroll lentamente, necesario para cargar todos los datos.

        :param speed: int - Establece la velocidad con la cual hace el scroll
        :return: None
        """
        current_scroll_position, new_height = 0, 1
        while current_scroll_position <= new_height:
            current_scroll_position += speed
            self.driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
            new_height = self.driver.execute_script("return document.body.scrollHeight")
