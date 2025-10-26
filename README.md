# ScanSQLi - SQL Injection Patch Scanner

![banner](https://img.shields.io/badge/version-1.0-green.svg)
![python](https://img.shields.io/badge/python-3.x-blue.svg)
![license](https://img.shields.io/badge/license-MIT-yellow.svg)

**ScanSQLi** is a lightweight multi-threaded SQL Injection vulnerability scanner written in Python.  
It checks multiple target URLs and parameters for possible SQL injection points using custom payload lists.

---

## 🧠 Features
- Fast multi-threaded SQLi vulnerability scanning  
- Works on both Linux and Termux  
- Customizable target list, parameters, and payloads  
- Saves vulnerable URLs into `Vuln.txt`  
- Colored CLI output for better visibility  

---

## 🔗 Repository
**GitHub:** [https://github.com/hmei7-id/sqli_scanner](https://github.com/hmei7-id/sqli_scanner)

---

## ⚙️ Requirements

### For Linux / Termux
- Python 3.x  
- `pip` package manager  

Install dependencies:
```bash
pip install -r requirements.txt
