# 🕷️ ScanSQLi — SQL Injection Patch Scanner

![version](https://img.shields.io/badge/version-1.0-green.svg)
![python](https://img.shields.io/badge/python-3.x-blue.svg)
![license](https://img.shields.io/badge/license-MIT-yellow.svg)
![platform](https://img.shields.io/badge/platform-Linux%20%7C%20Termux-blue.svg)

---

## 📖 Overview

**ScanSQLi** is a lightweight, multithreaded SQL Injection (SQLi) scanner written in Python.  
It tests multiple target URLs, parameters, and payloads concurrently to detect potential SQL injection vulnerabilities.

Intended audience: penetration testers, web security researchers, educators. Use responsibly and only on systems you are authorized to test.

**Repository:** https://github.com/hmei7-id/sqli_scanner

---

## ⚠️ Disclaimer

This tool is for **ethical** security testing and educational purposes only. Do **not** scan or attack systems without explicit permission. The author is not liable for misuse.

---

## 🧩 Features

- Multi-threaded scanning for faster checks  
- File-driven input (targets, params, payloads)  
- Colored terminal output (Green = Vulnerable, Red = Not vulnerable)  
- Saves results automatically to `Vuln.txt`  
- Works on Linux, Termux (Android), and Windows (with Python 3)

---

## 📦 Requirements

- Python 3.6+  
- pip

External Python packages (listed in `requirements.txt`):

```
requests
colorama
```

Install all requirements:
```bash
pip install -r requirements.txt
```

---

## 🔧 Installation (First Time)

### Linux / Termux / macOS

1. Clone the repository:
```bash
git clone https://github.com/hmei7-id/sqli_scanner.git
```

2. Change directory:
```bash
cd sqli_scanner
```

3. (Optional but recommended) Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate    # Linux / Termux / macOS
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

### Windows (Optional)

1. Clone and change directory:
```powershell
git clone https://github.com/hmei7-id/sqli_scanner.git
cd sqli_scanner
```

2. (Optional) Create and activate virtual environment:
```powershell
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```powershell
pip install -r requirements.txt
```

---

## ▶️ Usage (First Run)

Run the scanner:
```bash
python3 Scan.py
```

You will be asked interactively for:

- `Website files`: path to a file containing target sites (one per line) — e.g. `websites.txt`  
- `Parameter File (Mysql.txt)`: path to a file containing parameter endpoints — e.g. `Mysql.txt`  
- `SQLi Payload File (sql1.txt or sql2.txt)`: path to payload list — e.g. `sql1.txt`  
- `Number of threads (10-20)`: integer (recommended 5–20)

Example prompt:
```
[!] Enter Website files: websites.txt
[!] Input Parameter File (Mysql.txt):
[!] Input SQLi Payload File (sql1.txt or sql2.txt):
[!] Enter number of threads (10-20): 10
```

The script will scan and print results to the terminal and save vulnerable URLs to `Vuln.txt`.

---

## 💾 Example Input Files

Create these example files in the project folder before running the scanner.

**websites.txt**
```
https://testphp.vulnweb.com
https://example.com
http://192.168.1.10
```

**Mysql.txt**
```
index.php?id=
product.php?id=
category.php?id=
page.php?page=
```

**sql1.txt**
```
'
" or "1"="1
' OR '1'='1
-- -
' OR 'a'='a
```

---

## 🔍 Output

- Vulnerable endpoints printed in **green**:
```
[+] VULN: https://testphp.vulnweb.com/product.php?id='
```
- Non-vulnerable endpoints printed in **red**.
- All vulnerable URLs are saved to `Vuln.txt` (one per line).

---

## ⚙️ Tuning & Recommendations

- Increase `num_threads` for faster scanning, but monitor CPU & network usage. Typical: `5–20`.  
- Start with small payload lists for an initial sweep; expand payloads for deeper testing.  
- Use a proxy (Burp Suite, OWASP ZAP) for verification and to throttle/record traffic.  
- Always obtain written permission before scanning third-party targets.

---

## 🧪 Tested Platforms

- Kali Linux — ✅  
- Ubuntu — ✅  
- Termux (Android) — ✅  
- Windows 10/11 — ✅ (color support may vary)

---

## 🛠️ Troubleshooting

- `ModuleNotFoundError`: run `pip install -r requirements.txt`.  
- Colors not visible on Windows: try Windows Terminal or enable ANSI support.  
- Network errors: ensure targets are reachable and not blocked by firewall.

---

## 📚 Development & Contribution

Contributions, issues, and feature requests are welcome. Please open issues or PRs on the repository:

https://github.com/hmei7-id/sqli_scanner

---

## 👨‍💻 Author

**Herlambang Ichtiarto (Lam)**  
GitHub: https://github.com/hmei7-id

---

## 📜 License

This project is distributed under the **MIT License**. See `LICENSE` for details.
