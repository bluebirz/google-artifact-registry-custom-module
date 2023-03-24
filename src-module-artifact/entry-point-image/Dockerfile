FROM python:slim
WORKDIR /usr/src/app
COPY src/ ./src
ARG TOKEN
RUN awk '{gsub("https://", "https://oauth2accesstoken:${TOKEN}@", $0); print}' src/requirements.txt > src/tokenized_requirements.txt
RUN [ "pip", "install", "-r", "src/tokenized_requirements.txt" ]
RUN [ "rm", "src/tokenized_requirements.txt"]
CMD [ "python3", "src/main.py"]