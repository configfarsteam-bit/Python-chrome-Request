FROM python:3.12-slim

RUN apt-get update && apt-get install -y wget ca-certificates \
    && wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir selenium

WORKDIR /app
COPY visit.py .

ENV TARGET_URL=https://example.com
CMD ["python", "-u", "visit.py"]
