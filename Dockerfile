from turnerlabs/azure-chaqer-base

ADD . /opt/

CMD [ "python", "/opt/identifyFacesS3Bucket.py" ]
