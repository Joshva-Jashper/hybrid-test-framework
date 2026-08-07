FROM ununtu:20.04
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/joshvajaspher6-dotcom/hybrid-test-framework.git .

RUN pip3 install --upgrade pip
RUN pip3 install playwright pytest
RUN playwright install --with-deps



CMD ["pytest", "-v", "-s"]

