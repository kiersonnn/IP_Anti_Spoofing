import socket
import struct
import ipaddress
import pyshark

def source_ip_check(source_ip,allowed_subnets):
    source_ip_object=ipaddress.ip.address(source_ip)
    for subnet in allowed_subnets:
        if source_ip_object in subnet:    ##checking if ip address is on subnet
            return True
    return False

def main(interface, allowed_subnets):
    capture = pyshark.LiveCapture(interface=interface, display_filter='ip')
    print(f"Listening on interface: {interface}")

    for packet in capture.sniff_continuously():
        try:
            src_ip = packet.ip.src #parser ip header
            if not source_ip_check(src_ip, allowed_subnets):
                print("Possible IP spoofing")

        except KeyboardInterrupt:
            print("Stop program")
            break
if __name__ == "__main__":
    interface = "\\Device\\NPF_{2F6D5BA2-155A-42D8-A8F6-BF6579D219BC}" #input interface
    allowed_subnets = [ipaddress.ip_network('192.168.1.0/24')]  #input subnet
    main(interface, allowed_subnets)

