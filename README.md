# Phishing Website Detector 🕵️

A web app that detects phishing websites by analyzing URL patterns and alerts users if a site is suspicious.

---

## 🔹 Features

- Checks for common phishing signs:
  - Missing HTTPS
  - Long URLs
  - Use of `-` in domain
  - `@` symbol in URL
  - Too many subdomains
  - Suspicious keywords (login, verify, update, secure, bank, free)
  - IP address in URL
- Provides a clear explanation why a URL is flagged.
- Displays a graph summarizing Safe vs Phishing URLs checked.
- Built with **Python** and **Streamlit**.

---

## 🔹 Demo

![Screenshot](screenshot.png)  
*(Replace `screenshot.png` with an actual screenshot of your app)*

---

## 🔹 Installation

1. Clone the repository:

```bash
git clone https://github.com/0xSouravXBT/phishing-website-detector.git
cd phishing-website-detector

2. Install dependencies:
pip install streamlit matplotlib

3. Run the app:
streamlit run phishing_detector.py
