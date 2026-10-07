# Network Security Scanner

A beginner-friendly Python tool that checks a small list of common TCP ports
on a hostname or IP address.

## Purpose

This project demonstrates basic networking and cybersecurity concepts:
- Hostname-to-IP resolution
- TCP socket connections
- Port scanning
- Identifying common network services

## Technologies

- Python 3
- `socket` standard library

## How to Run

```bash
python network_scanner.py
```

Enter a hostname or IP address when prompted.

For example, you can test a system you own or have permission to assess:

```text
localhost
```

## Ports Checked

The scanner checks a limited set of common ports, including:

- 21 - FTP
- 22 - SSH
- 53 - DNS
- 80 - HTTP
- 443 - HTTPS
- 3306 - MySQL
- 8080 - HTTP Alternate

## Example Output

```text
Target: localhost
IP address: 127.0.0.1

Scanning common TCP ports...
[OPEN]  22    SSH
[OPEN]  80    HTTP

Found 2 open common port(s).
```

## Ethical Use

Use this tool only on systems you own or have explicit permission to test.
It is designed for educational purposes and performs a limited scan of
common TCP ports.

## Learning Goals

This project was created as a beginner cybersecurity exercise to practice
Python sockets, networking fundamentals, and basic security assessment logic.
