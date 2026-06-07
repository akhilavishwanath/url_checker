# 🔐 URL Safety Checker

A simple and beginner-friendly cybersecurity project built using Python and Streamlit that helps users identify potentially suspicious or unsafe URLs using basic phishing detection rules.

---

# 📌 Project Overview

The URL Safety Checker is a lightweight web application designed to analyze URLs and detect common phishing or scam indicators.

The application checks links for suspicious patterns such as:

* Missing HTTPS
* Excessive URL length
* Presence of `@` symbols
* Suspicious keywords
* Too many dots/subdomains

Based on these checks, the system classifies URLs as:

* ✅ Safe
* ⚠️ Kinda Risky
* ❌ Scam

This project is useful for learning:

* Basic cybersecurity concepts
* URL validation techniques
* Phishing detection logic
* Streamlit web app development

---

# 🚀 Features

* URL safety analysis
* Suspicious pattern detection
* Risk scoring system
* Simple and interactive UI
* Beginner-friendly cybersecurity project
* Instant safety results

---

# 🛠️ Tech Stack

| Technology | Purpose            |
| ---------- | ------------------ |
| Python     | Backend Logic      |
| Streamlit  | Web Application UI |

---

# 🔍 Detection Rules

The system increases the risk score if:

* URL contains `@`
* URL is excessively long
* URL does not use HTTPS
* URL contains suspicious keywords like:

  * `login`
  * `bank`
* URL contains too many dots/subdomains

---

# 📂 Project Structure

```bash
url_checker/
│
├── app.py
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/akhilavishwanath/url_checker.git
```

## 2️⃣ Open Project Folder

```bash
cd url_checker
```

## 3️⃣ Install Requirements

```bash
pip install streamlit
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 💡 Usage

1. Open the Streamlit application
2. Paste any URL into the input box
3. Click **Check**
4. View the safety result and detected issues

---

# 🧠 Example Checks

| URL Type                         | Result   |
| -------------------------------- | -------- |
| Secure HTTPS link                | ✅ Safe   |
| Missing HTTPS                    | ⚠️ Risky |
| Suspicious banking/phishing link | ❌ Scam   |

---

# 📸 Sample Output

The application displays:

* Risk level
* Risk score
* Detected suspicious indicators

---

# 🎯 Learning Outcomes

This project helps understand:

* Basic phishing detection
* URL security concepts
* Cybersecurity fundamentals
* Python conditional logic
* Streamlit UI development

---

# 🔮 Future Enhancements

Possible future improvements:

* Machine learning-based phishing detection
* Domain reputation checking
* VirusTotal API integration
* Real-time blacklist checking
* Browser extension support
* Advanced URL parsing
* QR code scanning support

---

# 📜 License

This project is developed for educational and learning purposes.

---

# 👩‍💻 Author

Akhila Vishwanath
