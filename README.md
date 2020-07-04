# Running in a container

```
docker build --tag nlp_app:1.0 .
docker run -p 8501:8501 nlp_app:1.0
# docker run -it -p 8501:8501 nlp_app:1.0 /app/bin/example.py
```

# Running locally

```
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md
```