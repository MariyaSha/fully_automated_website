import json
import streamlit as st

st.title("👹 Tech Goblin")
st.caption("AI-curated tech news")

with open("articles.json", encoding="utf-8") as file:
    articles = json.load(file)

for i in articles:
    with st.expander(i["title"]):
        st.caption(
            i["source"] + " · " + i["pubDate"][:10]
            )
        st.write(i["contentSnippet"])
        st.link_button(
            "Read original source", i["link"]
            )
