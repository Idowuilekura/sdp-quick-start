FROM apache/spark:4.1.0-preview4

USER root

RUN apt-get update && apt-get install -y python3 python3-pip \ 
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install --no-cache-dir jupyterlab "pyspark[pipelines]" pyyaml \
    && wget https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-4.0_2.13/1.10.0/iceberg-spark-runtime-4.0_2.13-1.10.0.jar -P /opt/spark/jars

ENV PYSPARK_PYTHON=python3
WORKDIR /opt/app

EXPOSE 8888
# COPY ./app/entrypoint.sh /opt/app/entrypoint.sh && COPY ./app/test.py /opt/app/test.py && COPY ./app/pre_flight.py /opt/app/pre_flight.py
COPY ./app/entrypoint.sh ./app/test.py ./app/pre_flight.py /opt/app/

RUN chmod +x /opt/app/entrypoint.sh

CMD ["bash", "/opt/app/entrypoint.sh"]