# MITM (Man-in-the-Middle) Attack Toolkit

This project contains various tools designed to perform MITM (Man-in-the-Middle) attack scenarios. These tools utilize methods such as ARP spoofing, packet sniffing, DNS spoofing, and SSL redirection to analyze and manipulate network traffic.

> **Warning**: These tools are intended solely for educational and security testing purposes. Unauthorized MITM attacks are illegal. Please ensure you use these tools within a legal and ethical framework.

## Contents
- Features
- Requirements
- Installation
- Network Configuration
- Usage
  - ARP Spoofing
  - Packet Sniffing
  - SSL Redirection and DNS Spoofing
- Legal Disclaimer

## Features
- **ARP Spoofing**: Redirects network traffic between a target and gateway using ARP (Address Resolution Protocol) spoofing.
- **Packet Sniffing**: Allows for HTTP request and payload analysis via packet sniffing.
- **SSL Redirection**: Redirects HTTP traffic over SSL.
- **DNS Spoofing**: Enables DNS traffic manipulation and redirection using `dns2proxy`.

## Requirements
- **Python 3.x**
- **Scapy Library**
  - Install Scapy with:
    ```bash
    pip install scapy
    ```
- **Administrative Privileges**
  - Required for ARP spoofing and enabling IP forwarding.

## Installation
To set up this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/FurkanRecber/MITM.git
    ```

2. Navigate to the project directory:
    ```bash
    cd MITM
    ```

3. Install the necessary libraries:
    ```bash
    pip install scapy
    ```

4. Download the `dns2proxy` and `sslstrip2` submodules:
    ```bash
    git submodule update --init --recursive
    ```

## Network Configuration

To enable packet forwarding, IP forwarding must be enabled on your machine:

- **Linux**:
    ```bash
    echo 1 > /proc/sys/net/ipv4/ip_forward
    ```
- **macOS**:
    ```bash
    sysctl -w net.inet.ip.forwarding=1
    ```
- **Windows**:
    ```bash
    netsh interface ipv4 set interface "INTERFACE_NAME" forwarding=enabled
    ```
    Replace `INTERFACE_NAME` with your network interface name.

## Usage

### ARP Spoofing
This section explains how to perform ARP spoofing using the `arp_spoofing.py` script.

#### Script Parameters
The script requires the following arguments:
- `-t` or `--target`: IP address of the target device.
- `-g` or `--gateway`: IP address of the gateway (typically the router).
The script will continuously send ARP poison packets to redirect traffic between the target and gateway. To stop, use `Ctrl+C`; the ARP tables will automatically reset to their original state.

## Packet Sniffing
This section explains how to capture HTTP traffic on a network interface using the `packet_listener.py` script.

### Script Parameters
- `-i` or `--interface`: Network interface to capture packets from.

### Example Command
Run the script specifying the network interface:

```bash
sudo python packet_listener.py -i wlan0
```  

#### Example Command
Run the script with administrative privileges:
```bash
sudo python arp_spoofing.py -t 192.168.1.5 -g 192.168.1.1
```
The script will listen for HTTP requests and print the payloads.

## SSL Redirection and DNS Spoofing
This section explains how to perform SSL redirection and DNS spoofing by setting up `iptables` rules to redirect traffic.

### SSL Redirection (Using sslstrip2)
Redirect HTTP traffic to port 1000 using the following `iptables` rule:

```bash
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 1000
```

This allows tools like `sslstrip2` to intercept HTTP traffic.

### DNS Spoofing (Using dns2proxy)
To redirect DNS traffic to `dns2proxy`, use this rule:

```bash
iptables -t nat -A PREROUTING -p udp --destination-port 53 -j REDIRECT --to-port 53
```
Incoming DNS traffic will be redirected through `dns2proxy` for manipulation.

## Legal Disclaimer
This tool is intended for educational and security testing purposes only. Unauthorized MITM attacks are illegal. Obtain proper authorization before using this tool, and always adhere to laws and ethical guidelines.
