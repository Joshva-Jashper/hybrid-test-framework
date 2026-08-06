FROM ubuntu:20.04
RUN apt update && apt upgrade -y
RUN apt install python3 -y
RUN apt install python3-pip  git curl pytest -y
RUN pip install playwright
RUN playwright install --with-deps

WORKDIR /app

CMD ["pytest","-v","-s","tests"]


