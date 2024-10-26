FROM python:alpine3.19
LABEL maintainer="office@bizeducate.com"

WORKDIR /bizeducate_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


# copy entrypoint.sh
COPY ./entrypoint.sh .
#RUN sed -i 's/\r$//g' /bizeducate_app/entrypoint.sh
RUN chmod +x /bizeducate_app/entrypoint.sh

# Create the appropriate directories
ENV APP_HOME=/bizeducate_app/web
RUN mkdir -p $APP_HOME/staticfiles
WORKDIR $APP_HOME

ENV APP_HOME=/bizeducate_app/web
RUN mkdir -p $APP_HOME/media
WORKDIR $APP_HOME

COPY . .

# create the app user and group
RUN addgroup --system bizeducate_app && adduser --system --ingroup bizeducate_app bizeducate_app

# chown all the files to the app user
RUN chown -R bizeducate_app:bizeducate_app /bizeducate_app

# change to the app user
USER bizeducate_app

# run entrypoint.sh
ENTRYPOINT ["/bizeducate_app/entrypoint.sh"]
