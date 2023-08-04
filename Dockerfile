FROM python:3.11.3


SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

RUN pip install --upgrade pip

RUN useradd -rms /bin/bash stgr && chmod 777 /opt /run

WORKDIR /stgr

RUN mkdir /stgr/static && mkdir /stgr/media && chown -R stgr:stgr /stgr && chmod 755 /stgr

COPY --chown=stgr:stgr . .

RUN pip install -r requirements.txt

USER stgr

CMD ["gunicorn", "-b", "0.0.0.0:8000", "stogram_backend.wsgi:application"]