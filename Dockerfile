FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /build

COPY requirements.txt .
RUN pip install -r requirements.txt

# COPY ./app ./app

CMD [ "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0" ]

EXPOSE 8000