import traceback

from django.shortcuts import render
from django.views import View
from .scraper_views import Scraper


class ScrapingView(View):
    """
    Clase encargada de procesar las solicitudes http del cliente
    :var : template_name: string - contiene la ruta del template
    """
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        """
        Método de vista para manejar solicitudes POST. Procesa las credenciales de inicio de sesión proporcionadas en la solicitud,
        realiza scraping utilizando las credenciales proporcionadas y renderiza la página de resultados.

        :param request: El objeto de solicitud HTTP
        :param args: Argumentos posicionales adicionales
        :param kwargs: Argumentos de palabras clave adicionales
        :return: HttpResponse - Página de resultados renderizada con los datos extraídos o un mensaje de error
        """

        username = request.POST['username']
        password = request.POST['password']

        context = {
            'username': username,
            'password': password,
        }
        if username and password:
            try:
                scraper = Scraper()
                scraper.load_page('https://bandcamp.com/login?from=menubar')
                scraper.login(username, password)
                context['data'] = scraper.process()
                scraper.driver_view.quit_driver()
            except Exception as e:
                error_message = str(e.__str__())

                print('//////////////////////////////////////////////////////////////////////')
                traceback.print_exc()
                print('//////////////////////////////////////////////////////////////////////')

                return render(request, 'results.html', {'error_message': error_message})

        return render(request, 'results.html', context)

    def get(self, request, *args, **kwargs):
        """
        Método de vista para manejar solicitudes GET. Renderiza la página index.html desde donde se introducen los datos para realizar el scrapin.

        :param request: El objeto de solicitud HTTP
        :param args: Argumentos posicionales adicionales
        :param kwargs: Argumentos de palabras clave adicionales
        :return: HttpResponse - Página index.html renderizada
        """
        return render(request, 'index.html')
