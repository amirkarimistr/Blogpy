FROM python:3.8

ENV PYTHONUNBUFFERED 1
RUN mkdir /blogpy
WORKDIR /blogpy
COPY . /blogpy

ADD requirenments/requirenment.txt /blogpy
RUN pip install --upgrade pip
RUN pip install -r requirenment.txt

RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "blogpy", "--bind", ":8000", "blogpy.wsgi:application"]

