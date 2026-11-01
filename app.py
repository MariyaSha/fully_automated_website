import json
import streamlit as st

st.title("👹 Tech Goblin")
st.caption("AI-curated tech news")

with open("articles.json", encoding="utf-8") as file:
    articles = json.load(file)

for article in articles:
    with st.expander(article["title"]):
        st.caption(article["source"] + " · " + article["published_at"][:10])
        st.write(article["summary"])
        st.link_button("Read original source", article["url"])
