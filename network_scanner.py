import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt",
}

def scan_host(host, timeout=0.5):
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Host could not be resolved.")
        return

    print(f"Target: {host}")
    print(f"IP address: {ip}")
    print("\nScanning common TCP ports...")

    open_ports = []

    for port, service in COMMON_PORTS.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        try:
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append((port, service))
                print(f"[OPEN]  {port:<5} {service}")
        finally:
            sock.close()

    if not open_ports:
        print("[INFO] No common open TCP ports detected.")
    else:
        print(f"\nFound {len(open_ports)} open common port(s).")


def main():
    host = input("Enter a hostname or IP address: ").strip()

    if not host:
        print("Please enter a valid hostname or IP address.")
        return

    scan_host(host)


if __name__ == "__main__":
    main()
