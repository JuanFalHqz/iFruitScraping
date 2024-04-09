FROM python:3.12

ENV PYTHONUNBUFFERED=1

# Instala dependencias necesarias para Chrome y Selenium
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    libnss3 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libxcomposite1 \
    libxdamage1 \
    libgbm1 \
    libxrandr2 \
    libasound2 \
    libatk1.0-0 \
    libgtk-3-0 \
    libgbm1 \
    fonts-liberation \
    libxshmfence1 \
    --no-install-recommends

# Descarga e instala Chrome
RUN wget -q -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i /tmp/chrome.deb; apt-get -fy install

# Instala el controlador de Selenium (en este caso, para Chrome)
RUN apt-get update && apt-get install -y chromium-driver

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]