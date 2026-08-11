FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/joshvajaspher6-dotcom/hybrid-test-framework.git .

RUN python3 -m pip install --upgrade pip --break-system-packages
RUN pip3 install --break-system-packages playwright pytest
RUN playwright install --with-deps

CMD ["pytest", "-v", "-s"]