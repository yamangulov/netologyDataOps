FROM continuumio/miniconda3:latest

RUN mkdir /app
WORKDIR /app
COPY 1.sh /app
RUN chmod +x 1.sh
RUN conda config --append channels conda-forge
RUN conda install python mlflow boto3 pymysql
RUN bash 1.sh