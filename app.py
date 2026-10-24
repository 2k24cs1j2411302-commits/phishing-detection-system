import re
import streamlit as st
import joblib

model = joblib.load("phishing_model.pkl")

url = st.text_input("URL daalo:")

if url:
    d = len(url)
    dots = url.count(".")
    digits = sum(c.isdigit() for c in url)
    at = 1 if "@" in url else 0
    https = 1 if url.startswith("https") else 0
    special = sum(url.count(c) for c in "%@=&?_-")
    ip = 1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 0

    pred = model.predict([[d, dots, digits, at, https, special, ip]])[0]

    if pred == 1:
        st.error("🚨 PHISHING DETECTED")
    else:
        st.success("✅ SECURE")
