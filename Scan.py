import requests
import threading
import os
from colorama import Fore, Style, init

init(autoreset=True)

os.system("cls" if os.name == "nt" else "clear")

banner = r"""
 ____                  ____   ___  _     _ 
/ ___|  ___ __ _ _ __ / ___| / _ \| |   (_)
\___ \ / __/ _` | '_ \\___ \| | | | |   | |
 ___) | (_| (_| | | | |___) | |_| | |___| |
|____/ \___\__,_|_| |_|____/ \__\_\_____|_|
    """
print(Fore.MAGENTA + banner)
print(Fore.YELLOW + "      [+]  ScanSQLi - SQL Injection Patch Scanner  [+]\n" + Style.RESET_ALL)

def check_sql_injection(website, params, payloads, found_vulns):
    for param in params:
        for payload in payloads:
            URL = f"{website.strip()}/{param.strip()}{payload.strip()}"
            try:
                response = requests.get(URL)
                if response.status_code == 200 and "error" in response.text.lower():
                    found_vulns.add(URL)
                    print(Fore.GREEN + f"[+] VULN: {URL}")
                else:
                    print(Fore.RED + f"[-] NOT VULN: {URL}")

            except Exception:
                continue

def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def main():
    site_file = input(Fore.BLUE + "[!] Enter Website files: " + Style.RESET_ALL)
    param_file = input(Fore.BLUE + "[!] Input Parameter File (Mysql.txt): " + Style.RESET_ALL)
    payload_file = input(Fore.BLUE + "[!] Input SQLi Payload File (sql1.txt or sql2.txt): " + Style.RESET_ALL)
    num_threads = int(input(Fore.BLUE + "[!] Enter number of threads (10-20): " + Style.RESET_ALL) or 5)
    
    print(Fore.YELLOW + f"[!]    Starting Scanning    [!]")
    websites = read_file(site_file)
    parameters = read_file(param_file)
    payloads = read_file(payload_file)

    threads = []
    found_vulns = set()

    for website in websites:
        thread = threading.Thread(target=check_sql_injection, args=(website, parameters, payloads, found_vulns))
        threads.append(thread)
        thread.start()

        if len(threads) >= num_threads:
            for thread in threads:
                thread.join()
            threads = []

    for thread in threads:
        thread.join()

    with open('Vuln.txt', 'w') as vuln_file:
        for vuln in found_vulns:
            vuln_file.write(f"{vuln}\n")

if __name__ == "__main__":
    main()