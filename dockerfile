FROM --platform=linux/amd64 python:3
ARG port

ADD . /PYTHON-OC-LETTINGS-FR/
WORKDIR /PYTHON-OC-LETTINGS-FR/

ENV PORT=$port

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    && apt-get -y install curl \
    && apt-get install libgomp1

RUN chgrp -R 0 /PYTHON-OC-LETTINGS-FR \
    && chmod -R g=u /PYTHON-OC-LETTINGS-FR \
    && pip install pip --upgrade \
    && pip install -r requirements.txt
EXPOSE $PORT

CMD gunicorn oc_lettings_site.wsgi:server --bind 0.0.0.0:$PORT --preload
