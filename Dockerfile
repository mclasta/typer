FROM python:3.13.5

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH=/app

WORKDIR /app

RUN apt-get update && apt-get install -y \
    xclip xsel kbd \
    libx11-dev libxtst-dev libxrandr-dev libxi-dev \
    build-essential linux-headers-amd64 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/

CMD ["python", "-m", "app.main"]
