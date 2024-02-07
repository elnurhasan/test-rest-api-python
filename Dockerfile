FROM python:3.11.5-bullseye
ENV env_settings=prod
ENV DJANGO_SETTINGS_MODULE=test_api.settings
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip setuptools
RUN pip install --default 1000 -r requirements.txt
