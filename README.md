# 🕷️ ScanSQLi - SQL Injection Patch Scanner

![version](https://img.shields.io/badge/version-1.0-green.svg)
![python](https://img.shields.io/badge/python-3.x-blue.svg)
![license](https://img.shields.io/badge/license-MIT-yellow.svg)
![platform](https://img.shields.io/badge/platform-Linux%20%7C%20Termux-blue.svg)

---

## 📖 Overview

**ScanSQLi** is a lightweight, multithreaded SQL Injection (SQLi) scanner written in Python.  
It tests multiple target URLs, parameters, and payloads concurrently to detect potential SQL injection vulnerabilities.

This tool is intended for penetration testers, web security researchers, and educators. Use responsibly and only on systems you are authorized to test.

**Repository:** https://github.com/hmei7-id/sqli_scanner

---

## ⚠️ Disclaimer

This tool is for **ethical** security testing and educational purposes only. Do **not** scan or attack systems without explicit permission. The author is not liable for misuse.

---

## 🧩 Features

- Multi-threaded scanning for faster checks  
- Simple, file-driven input (targets, params, payloads)  
- Colored terminal output (Green = Vulnerable, Red = Not vulnerable)  
- Saves results automatically to `Vuln.txt`  
- Works on Linux, Termux (Android), and Windows (with Python 3)

---

## 📦 Requirements

- Python 3.6+  
- pip

External Python packages:



You can install requirements with:
```bash
pip install -r requirements.txt


🔧 Installation (First Time) — Linux / Termux / macOS

Clone the repository:

git clone https://github.com/hmei7-id/sqli_scanner.git


Change directory:

cd sqli_scanner


(Optional) Create a virtual environment (recommended):

python3 -m venv venv
source venv/bin/activate    # Linux / Termux / macOS


Install dependencies:

pip install -r requirements.txt

🪟 Installation (Windows)

Clone the repository:

git clone https://github.com/hmei7-id/sqli_scanner.git
cd sqli_scanner


(Optional) Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt

▶️ Usage (First Run)

Run the scanner:

python3 Scan.py


When prompted, provide file paths (one per prompt):

[!] Enter Website files: websites.txt
[!] Input Parameter File (Mysql.txt):
[!] Input SQLi Payload File (sql1.txt or sql2.txt):
[!] Enter number of threads (10-20): 10


websites.txt — a list of target base URLs (one per line). Example:

https://example.com
https://testphp.vulnweb.com
192.168.1.10


Mysql.txt — list of parameter endpoints to test. Example:

index.php?id=
product.php?id=
page.php?page=


sql1.txt / sql2.txt — payload strings to append to parameters. Example:

'
" or "1"="1
' OR '1'='1
-- -


The scanner will print results to the terminal and save found vulnerable URLs to Vuln.txt.

💾 Example Files (Create these before running)

websites.txt

https://testphp.vulnweb.com
https://example.com


Mysql.txt

index.php?id=
product.php?id=
category.php?id=


sql1.txt

'
" or "1"="1
' OR 'a'='a
-- -

🧰 Command-line Options (Script Prompts)

The script Scan.py is interactive and will prompt for:

Website list file path

Parameter list file path

Payload list file path

Number of threads to use (recommended 5–20 depending on system/network)

🔍 Output

Vulnerable endpoints are shown in green:

[+] VULN: https://testphp.vulnweb.com/product.php?id='


Non-vulnerable endpoints shown in red.

All vulnerable URLs are written to Vuln.txt (one per line).

⚙️ Tuning & Recommendations

Increase num_threads for faster scanning but monitor CPU and bandwidth. Typical values: 5-20.

Use a limited payload list for initial scans; expand payloads for deeper testing.

Consider using a proxy (Burp Suite, OWASP ZAP) for deeper analysis and to avoid noisy scans.

Always obtain permission before scanning a third-party target.

🧪 Tested Platforms

Kali Linux — ✅

Ubuntu — ✅

Termux (Android) — ✅

Windows 10/11 — ✅ (CLI colors may vary)

🛠️ Troubleshooting

ModuleNotFoundError: ensure you installed dependencies pip install -r requirements.txt.

Colors not showing on Windows: use Windows Terminal or enable ANSI escape support.

Network errors: ensure targets are reachable and no firewall blocks outbound requests.

📚 Development & Contribution

Contributions, issues, and feature requests are welcome. Please open issues or PRs on the repository:
https://github.com/hmei7-id/sqli_scanner
