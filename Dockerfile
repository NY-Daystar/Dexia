FROM python:3.11.4-slim

WORKDIR /usr/src/app

# Copy dependencies
COPY requirements.txt ./

# Install dependencies
RUN pip3 install -r requirements.txt \
    && rm -rf .cache/pip

COPY . .

WORKDIR /usr/src/app/api

CMD ["uvicorn", "setup:app", "--host", "0.0.0.0", "--port", "8080"]

## TODO suivre ce doc https://fastapi.tiangolo.com/deployment/docker/#dockerfile
