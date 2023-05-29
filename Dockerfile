FROM python:3.8.16

WORKDIR /app

RUN wget https://github.com/mitsuhiko/rye/releases/latest/download/rye-x86_64-linux.gz && \
    gunzip rye-x86_64-linux.gz && \
    mv ./rye* /usr/local/bin/rye && \
    chmod +x /usr/local/bin/rye && \
    rm -rf rye-x86_64-linux.gz 

COPY README.md README.md
COPY pyproject.toml pyproject.toml
COPY requirements-dev.lock requirements-dev.lock

RUN rye sync --no-lock
