# ARP Spoofing Script
This project is a Python-based ARP Spoofing Tool designed for educational and ethical hacking purposes. The script allows you to perform ARP (Address Resolution Protocol) spoofing to intercept network traffic between a target device and the gateway.

## Features
Redirects traffic between a target and a gateway through the attacker's machine using ARP poisoning.
Periodically sends ARP poison packets to maintain the redirection.
Resets the ARP tables on exit to restore normal network operation.

## Requirements
- Python 3.x
- Scapy Library
  - **Install using:**
```bash
pip install scapy
```
- Administrative Privileges  
  (Required to execute ARP spoofing and enable IP forwarding).

## Installation
- Clone the repository:
```bash
git clone https://github.com/FurkanRecber/MITM.git
```

- Navigate to the project directory:
```bash
cd MITM
```

- Ensure Scapy is installed:
```bash
pip install scapy
```

## Network Configuration
#### Enable IP Forwarding
IP forwarding must be enabled on the attacker's machine to allow intercepted traffic to pass through.

**Linux**
```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
```
**macOS**
```bash
sysctl -w net.inet.ip.forwarding=1
```
**Windows**  
Run the following command to enable routing:
```bash
netsh interface ipv4 set interface "INTERFACE_NAME" forwarding=enabled
```
Replace `"INTERFACE_NAME"` with your network interface name.

## Usage
#### Script Arguments
The script requires the following arguments to run:

- -t or --target: The IP address of the target machine.
- -g or --gateway: The IP address of the gateway (usually the router).

#### Example Command
Run the script with administrative privileges:
```bash
sudo python arp_spoof.py -t 192.168.1.5 -g 192.168.1.1
```

## Termination
Press Ctrl+C to stop the script. The ARP tables on the target and gateway will automatically be restored to their original state.

## Legal Disclaimer
This tool is intended for educational purposes only.
Unauthorized use of this script on a network without explicit permission is both illegal and unethical. Use this tool responsibly and always ensure you have proper authorization before using it in a penetration testing scenario.

## Troubleshooting
- Permission Denied: Ensure you run the script with administrative privileges (e.g., using sudo).
- Module Not Found: Install the Scapy library with:
```bash
pip install scapy
```
- Traffic Not Forwarding: Double-check that IP forwarding is enabled on your machine.
