import os
import urllib.parse

from dotenv import load_dotenv
import requests
import spacy_streamlit
import streamlit as st

load_dotenv()

token_headers = {"Authorization": f"Bearer {os.environ['ACCESS_TOKEN']}"}
api_url = urllib.parse.urljoin(os.environ["DBAPI_URL"], os.environ["DBAPI_STAGE"])

models = ["en_core_web_sm", "en_core_web_md"]

search_query = st.text_input("Input your search query here:", "query")
resp = requests.get(
    f"{api_url}/documents/search_summary?query={search_query}",
    headers=token_headers,
).json()
id_to_text = {}
for d in resp:
    id_to_text[d["id"]] = (d["title"].strip() + "\n" + d["parsed_text"]).strip()

id_ = st.selectbox("Select document", sorted(id_to_text.keys()))

default_text = id_to_text[id_]
st.text(default_text)
spacy_streamlit.visualize(models, default_text, visualizers=["ner"])
