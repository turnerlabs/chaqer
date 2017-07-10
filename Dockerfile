from turnerlabs/azure-chaqer-base

ADD . /opt/

CMD [ "python", "-t", "/opt/identifyFacesS3Bucket.py" ]
