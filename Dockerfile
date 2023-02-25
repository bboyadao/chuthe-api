FROM python:3.10-slim

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false \
  && poetry install $(test "$CHUTHE_ENV" == PROD && echo "--no-dev") --no-interaction
RUN chmod +x entrypoint.sh
CMD ["/bin/bash", "entrypoint.sh"]
