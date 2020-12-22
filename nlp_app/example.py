import requests
import spacy_streamlit
import streamlit as st

models = ["en_core_web_sm", "en_core_web_md"]
resp = requests.get("http://127.0.0.1:8000/documents/?skip=0&limit=5").json()
id_to_text = {}
for d in resp:
    id_to_text[d["id"]] = (d["title"].strip() + "\n" + d["parsed_text"]).strip()

id_ = st.selectbox("Select document", sorted(id_to_text.keys()))
default_text = id_to_text[id_]
spacy_streamlit.visualize(models, default_text, visualizers=["ner"])
