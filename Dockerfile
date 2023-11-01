FROM ghcr.io/osgeo/gdal:ubuntu-small-3.6.4 as base-all
LABEL maintainer Camptocamp "info@camptocamp.com"
SHELL ["/bin/bash", "-o", "pipefail", "-cux"]

COPY .nvmrc /tmp
# hadolint ignore=DL3008,SC1091
RUN --mount=type=cache,target=/var/lib/apt/lists \
    --mount=type=cache,target=/var/cache,sharing=locked \
    --mount=type=cache,target=/root/.cache \
    apt-get update \
    && apt-get install --yes --no-install-recommends python3-pip python3-dev libpq-dev gcc gnupg \
    && . /etc/os-release \
    && NODE_MAJOR="$(cat /tmp/.nvmrc)" \
    && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_${NODE_MAJOR}.x nodistro main" > /etc/apt/sources.list.d/nodesource.list \
    && curl --silent https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor --output=/etc/apt/keyrings/nodesource.gpg \
    && apt-get update \
    && apt-get install --assume-yes --no-install-recommends "nodejs=${NODE_MAJOR}.*" \
        libx11-6 libx11-xcb1 libxcomposite1 libxcursor1 \
        libxdamage1 libxext6 libxi6 libxtst6 libnss3 libcups2 libxss1 libxrandr2 libasound2 libatk1.0-0 \
        libatk-bridge2.0-0 libpangocairo-1.0-0 libgtk-3.0 libxcb-dri3-0 libgbm1 libxshmfence1

# Used to convert the locked packages by poetry to pip requirements format
# We don't directly use `poetry install` because it force to use a virtual environment.
FROM base-all as poetry

# Install Poetry
WORKDIR /poetry
COPY requirements.txt ./
# hadolint ignore=DL3042
RUN --mount=type=cache,target=/root/.cache \
    python3 -m pip install --disable-pip-version-check --requirement=requirements.txt

# Do the conversion
COPY poetry.lock pyproject.toml ./
ENV POETRY_DYNAMIC_VERSIONING_BYPASS=0.0.0
RUN poetry export --extras=application --with=dev --output=/poetry/requirements.txt

# Base, the biggest thing is to install the Python packages
FROM base-all as run

WORKDIR /app

# hadolint ignore=DL3042
RUN --mount=type=cache,target=/root/.cache \
    --mount=type=bind,from=poetry,source=/poetry,target=/poetry \
    python3 -m pip install --disable-pip-version-check --no-deps --requirement=/poetry/requirements.txt \
    && python3 -m pip freeze > /requirements.txt

WORKDIR /opt/pyramid_ogcapi
COPY pyramid_ogcapi ./pyramid_ogcapi
COPY pyproject.toml README.md ./
# hadolint ignore=DL3042
RUN --mount=type=cache,target=/root/.cache \
  pip install --disable-pip-version-check --no-deps .

WORKDIR /app
COPY acceptance_tests/pyramid_ogcapi_test_app ./pyramid_ogcapi_test_app
COPY acceptance_tests/pyproject.toml ./
# hadolint ignore=DL3042
RUN --mount=type=cache,target=/root/.cache \
  pip install --disable-pip-version-check --no-deps --editable=. \
  && python3 -m compileall -q .

COPY acceptance_tests/tests ./tests

COPY acceptance_tests/*.ini acceptance_tests/gunicorn.conf.py acceptance_tests/ogcapi-features-schema.yaml ./

CMD ["gunicorn", "--paste=application.ini"]

ENV \
  DEVELOPMENT=0 \
  SQLALCHEMY_POOL_RECYCLE=30 \
  SQLALCHEMY_POOL_SIZE=5 \
  SQLALCHEMY_MAX_OVERFLOW=25 \
  OTHER_LOG_LEVEL=WARNING \
  GUNICORN_LOG_LEVEL=WARNING \
  GUNICORN_ACCESS_LOG_LEVEL=INFO \
  SQL_LOG_LEVEL=WARNING \
  C2CWSGIUTILS_LOG_LEVEL=WARNING \
  LOG_LEVEL=INFO \
  PGOPTIONS=-c statement_timeout=1500 \
  GUNICORN_WORKERS=1 \
  GUNICORN_THREADS=10 \
  VISIBLE_ENTRY_POINT=/ \
  C2CWSGIUTILS_CONFIG=application.ini
