import socket
import sys

# MOST USED PORTS.
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-ALT"
}



# GETS THE IP
def resolve_target(target):
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        print("Error.")
        return None


def scan_ports(ip):
    print(f"\nScanning {ip}\n")

    for port, service in COMMON_PORTS.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"[OPEN] Port {port} ({service})")

        sock.close()


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <target>")
        return

    target = sys.argv[1]

    ip = resolve_target(target)

    if not ip:
        return

    print(f"Target: {target}")
    print(f"Resolved IP: {ip}")

    scan_ports(ip)


if __name__ == "__main__":
    main()