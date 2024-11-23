import scapy.all as scapy
from scapy.layers import http
import optparse


def get_user_input():
    opts = optparse.OptionParser()

    opts.add_option("-i", "--interface", dest="interface", help="Enter the interface to listen on")

    inputs = opts.parse_args()[0]

    if not inputs.interface:
        print("Interface must be specified")
    return inputs


def listen_packet(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)


def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)


user_input = get_user_input()
listen_packet(user_input.interface)
