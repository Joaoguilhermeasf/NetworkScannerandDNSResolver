# Network Scanner

Built to avoid spinning up nmap for simple checks. Pass a domain or IP,
it resolves the DNS and scans common ports (22, 80, 443, 8080 by default).

## Usage

# scan with default ports
python main.py google.com

# custom ports
python main.py google.com --ports 22,80,8080
