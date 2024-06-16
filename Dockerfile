FROM python:alpine3.19
LABEL maintainer="office@bizeducate.com"

WORKDIR /bizeducate_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
#RUN sed -i 's/\r$//g' /bizeducate_app/entrypoint.sh
RUN chmod +x /bizeducate_app/entrypoint.sh

COPY . .

# run entrypoint.sh
ENTRYPOINT ["/bizeducate_app/entrypoint.sh"]

#RUN mkdir -p /media
#
#RUN adduser \
#        --disabled-password \
#        --no-create-home \
#        django-user \
#    && chown -R django-user /media
#
#RUN chmod -R 755 /media
#
#USER django-user
