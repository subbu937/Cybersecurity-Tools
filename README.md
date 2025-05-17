# Cybersecurity Enumeration Tools

Welcome to my Cybersecurity Enumeration Tools repository! This project features two Python-based tools for network reconnaissance and cybersecurity analysis: a **DNS Enumeration Tool** and a **Subdomain Enumeration Tool**. Developed to strengthen my skills as an aspiring SOC Analyst, these tools demonstrate expertise in Python scripting, networking, and ethical hacking, complementing my experience with tools like Nmap, Splunk, and Burp Suite.

## About the Author
I’m Subhash Chandra Bose Vallapu, a cybersecurity enthusiast with a B.Tech in Mechanical Engineering (2020–2024) and three months of internship experience in cybersecurity and ethical hacking at CyberDosti. I specialize in Python, SQL, PL/SQL, SIEM, and network scanning, with a passion for securing digital infrastructure.  
- **GitHub**: [https://github.com/subbu937](https://github.com/subbu937)  
- **LinkedIn**: [https://www.linkedin.com/in/subhash-vallapu](https://www.linkedin.com/in/subhash-vallapu)  
- **Email**: subhashsubbu318@gmail.com  

## Tools Overview

### 1. DNS Enumeration Tool (`dns_enum.py`)
#### Description
The DNS Enumeration Tool automates querying DNS records (A, AAAA, NS, MX, TXT, SOA, etc.) for a target domain, providing insights into network configurations critical for cybersecurity reconnaissance and penetration testing.

#### Features
- Queries multiple DNS record types using the `dnspython` library.
- Handles errors (non-existent domains, no answers, Ctrl+C interrupts) robustly.
- Displays results in a user-friendly CLI with Pyfiglet formatting.
- Tested on public domains (e.g., youtube.com) for reliability.

#### Prerequisites
- Python 3.6+
- Libraries:
  ```bash
  pip install dnspython pyfiglet
  ```

#### Usage
```bash
python3 dns_enum.py <domainname>
```
Example:
```bash
python3 dns_enum.py youtube.com
```

#### Sample Output
```
 _____ _   _ ______  _____ 
|  __ \ \ | |  ____|/ ____|
| |  | \ \| | |__  | (___  
| |  | |\ ` |  __|  \___ \ 
| |__| | \  | |____ ____) |
|_____/   \_|______|_____/ 

A record for youtube.com
-----------------------
172.217.167.78
NS record for youtube.com
-----------------------
ns1.google.com
ns2.google.com
...
MX record for youtube.com
-----------------------
10 aspmx.l.google.com
...
```

### 2. Subdomain Enumeration Tool (`subdomain_enum.py`)
#### Description
The Subdomain Enumeration Tool discovers active subdomains of a target domain using multithreaded HTTP requests, aiding vulnerability assessments and penetration testing by identifying potential attack surface entry points.

#### Features
- Employs multithreading for efficient scanning of 614+ subdomains (via `subdomains.txt`).
- Validates domains with socket checks to avoid invalid inputs.
- Saves results to `discovered_subdomains.txt` for further analysis.
- Handles timeouts, connection errors, and user interrupts with color-coded output (green for successes, red for errors).

#### Prerequisites
- Python 3.6+
- Libraries:
  ```bash
  pip install requests pyfiglet
  ```
- A `subdomains.txt` file with 614 subdomains (included in the repository).

#### Setup
1. Ensure `subdomains.txt` (containing 614 common subdomains like `www`, `admin`, `api`) is in the script’s directory.
2. Install dependencies:
   ```bash
   pip install requests pyfiglet
   ```

#### Usage
```bash
python3 subdomain_enum.py <domainname>
```
Example:
```bash
python3 subdomain_enum.py youtube.com
```

#### Sample Output
```
  _____ _    _ ______  _____ 
 / ____| |  | |  ____|/ ____|
| |    | |__| | |__  | (___  
| |    |  __  |  __|  \___ \ 
| |____| |  | | |____ ____) |
 \_____|_|  |_|______|_____/ 

[+] Discovered subdomain: http://www.youtube.com
[-] Timeout on http://mail.youtube.com
[+] Discovered subdomain: http://api.youtube.com
...
end of tool
```

#### Output File
`discovered_subdomains.txt`:
```
http://www.youtube.com
http://api.youtube.com
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/subbu937/Cybersecurity-Tools.git
   cd Cybersecurity-Tools
   ```
2. Install dependencies:
   ```bash
   pip install dnspython pyfiglet requests
   ```
3. Verify `subdomains.txt` is present for the Subdomain Enumeration Tool.
4. Run the tools as shown in the Usage sections.

## Ethical Usage
- Use these tools **only for educational purposes or authorized testing**. Scanning domains without permission may violate laws or terms of service.
- Always obtain explicit consent from domain owners before use.

## Future Improvements
- **DNS Tool**: Add support for SPF/DMARC records and JSON/CSV output.
- **Subdomain Tool**: Include HTTPS support, integrate external APIs (e.g., VirusTotal), and add progress bars.
- Suggestions are welcome via GitHub Issues!

## Contributing
1. Fork the repository.
2. Create a branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
- **Email**: subhashsubbu318@gmail.com
- **GitHub Issues**: Open an issue in this repository.
- **LinkedIn**: [https://www.linkedin.com/in/subhash-vallapu](https://www.linkedin.com/in/subhash-vallapu)

Thank you for visiting my Cybersecurity Enumeration Tools repository!