import requests
import spacy_streamlit
import streamlit as st

models = ["en_core_web_sm", "en_core_web_md"]
resp = requests.get(
    "https://p55oroem7k.execute-api.eu-west-1.amazonaws.com/prod/articles/?skip=85&limit=20"
).json()
id_to_text = {}
for d in resp:
    id_to_text[d["id"]] = (d["title"].strip() + " " + d["summary"]).strip()

pmid = st.selectbox('Select article', sorted(id_to_text.keys()))
default_text = id_to_text[pmid]
spacy_streamlit.visualize(models, default_text)
