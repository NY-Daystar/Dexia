FROM python:3.11.4-slim

LABEL maintainer="Lucas Noga <lucas.noga@ilium.co>"

# App folder
WORKDIR /home/app

# Copy dependencies
COPY requirements.txt ./

# Install dependencies
RUN pip3 install -r requirements.txt \
    && rm -rf .cache/pip

# Copy python code
COPY . ./

# Expose for api
EXPOSE 8080

CMD [ "python3", "." ]
