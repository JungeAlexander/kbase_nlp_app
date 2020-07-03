FROM python:3.8.3-slim

EXPOSE 8501

WORKDIR /app
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python -m spacy download en_core_web_sm
RUN python -m spacy download en_core_web_md

COPY ./nlp_app bin/
ENTRYPOINT [ "streamlit", "run"]
CMD ["/app/bin/example.py"]