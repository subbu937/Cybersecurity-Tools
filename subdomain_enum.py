import requests
import threading
import sys
import pyfiglet
import socket

TITLE = pyfiglet.figlet_format("SUBDOMAIN ENUMATION TOOL")
print(TITLE)

try:
    target_domain = sys.argv[1]
except IndexError:
    print(r"Syntax Error - puthon3 subdomain_enum.py <domainname>")
    print(r"     example - python3 subdomain_enum.py youtube.com")
    quit()

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

try:
    socket.gethostbyname(target_domain)
except socket.gaierror:
    msg=f'{RED}{target_domain}{RESET} is not a valid domain please check the spelling of domain you entered'
    print(msg)
    print("_"*len(target_domain))
    sys.exit()

with open('Subdomains.txt') as file:
    subdomains=file.read().splitlines()

discover_subdomains = []

lock = threading.Lock()

def check_subdomain(subdomain):
    url=f'http://{subdomain}.{target_domain}'
    try:
        requests.get(url, timeout=3)
    except requests.exceptions.Timeout:
        print(f"[-] Timeout on {url}")
    except requests.ConnectionError:
        pass
    else:
        print(f'[+] Disovered subdomain: {GREEN}{url}{RESET}')
        with lock:
            discover_subdomains.append(url)

threads = []
try:
    for subdomain in subdomains:
        thread = threading.Thread(target=check_subdomain, args= (subdomain,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

except KeyboardInterrupt:
        print()
        msg="you stop the task by pressing ctl+c"
        print('-'*len(msg))
        print(f'{msg}')
        print('-'*len(msg))
        print()
        sys.exit(0)

with open("discovered_subdomains.txt","w") as f:
        for subdomain in discover_subdomains:
            print(subdomain, file=f)

print("end of tool")
