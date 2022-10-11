FROM python:3
RUN git clone https://github.com/AugustoKark/CRUDpersonaAK.git
WORKDIR /CRUDpersonaAK
RUN pip install -r requirements.txt
CMD ["python3","-m", "unittest"]