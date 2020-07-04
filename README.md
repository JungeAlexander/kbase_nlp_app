docker build --tag nlp_app:1.0 .
docker run -p 8501:8501 nlp_app:1.0
# docker run -it -p 8501:8501 nlp_app:1.0 /app/bin/example.py