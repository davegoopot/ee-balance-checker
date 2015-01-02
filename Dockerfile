FROM davegoopot/python
MAINTAINER Dave Potts <dave@goopot.co.uk>


WORKDIR /srv
ADD ./requirements.txt /srv/requirements.txt
RUN pip3 install -r /srv/requirements.txt
VOLUME /code
WORKDIR /code
