FROM python:3.10-slim

ADD ./server_example/install/requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt \
    --no-cache-dir --no-warn-script-location

ADD ./server_example server_example

EXPOSE 4050

ENTRYPOINT bash /server_example/install/run_server.sh
