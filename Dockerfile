FROM python:3.7.4
USER root
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD ["ddtrace-run", "python", "app.py"]