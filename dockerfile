FROM python:3.9-buster

#Copying the requirements.txt file from the local directory to the docker container.
COPY requirements.txt requirements.txt