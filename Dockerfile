FROM python:3.6

WORKDIR /srv

RUN python3 -m pip install \
    axe-selenium-python==2.1.6 \
    pytest==5.4.3

COPY . .

CMD python3 -m pytest
