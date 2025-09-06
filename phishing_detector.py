import re
import streamlit as st
import matplotlib.pyplot as plt

# Track results
safe_count = 0
phishing_count = 0

# Function to check phishing signs
def check_phishing(url):
    warnings = []

    # Rule 1: Check URL length
    if len(url) > 75:
        warnings.append("URL is too long")

    # Rule 2: Check for '-' in domain
    if "-" in url:
        warnings.append("Suspicious '-' in domain")

    # Rule 3: Check HTTPS
    if not url.startswith("https://"):
        warnings.append("No HTTPS (secure connection missing)")

    # Rule 4: Check for IP address in URL
    if re.match(r"^https?:\/\/\d+\.\d+\.\d+\.\d+", url):
        warnings.append("URL uses IP address instead of domain")

    # Rule 5: Check for '@' in URL
    if "@" in url:
        warnings.append("Contains '@' symbol (phishing trick)")

    # Rule 6: Too many subdomains
    if url.count(".") > 3:
        warnings.append("Too many subdomains (can be suspicious)")

    # Rule 7: Suspicious keywords
    suspicious_keywords = ["login", "verify", "update", "secure", "banking", "free", "bonus"]
    if any(keyword in url.lower() for keyword in suspicious_keywords):
        warnings.append("Contains suspicious keywords")

    # Final Result
    if warnings:
        return False, warnings
    else:
        return True, ["No suspicious signs found"]

# ---------------- Streamlit UI ---------------- #
st.title("🕵️ Phishing Website Detector")
st.write("Enter a website URL to check if it's safe or phishing.")

# Input field
url = st.text_input("Enter URL (e.g., https://example.com)")

if "safe_count" not in st.session_state:
    st.session_state.safe_count = 0
if "phishing_count" not in st.session_state:
    st.session_state.phishing_count = 0

# Button
if st.button("Check Website"):
    is_safe, reasons = check_phishing(url)

    if is_safe:
        st.success("✅ Safe Website")
        st.write("Reason:", reasons[0])
        st.session_state.safe_count += 1
    else:
        st.error("⚠️ Phishing Suspected")
        st.write("Reasons:")
        for r in reasons:
            st.write(f"- {r}")
        st.session_state.phishing_count += 1

# Show graph of results
if st.session_state.safe_count + st.session_state.phishing_count > 0:
    st.subheader("📊 Detection Summary")
    labels = ["Safe", "Phishing"]
    values = [st.session_state.safe_count, st.session_state.phishing_count]

    fig, ax = plt.subplots()
    ax.bar(labels, values, color=["green", "red"])
    ax.set_ylabel("Count")
    ax.set_title("Websites Checked")
    st.pyplot(fig)
