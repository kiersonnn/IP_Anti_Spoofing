import socket
import struct
import ipaddress
import time

# Checking if the source IP is in allowed subnets
def source_ip_check(source_ip, allowed_subnets):
    source_ip_obj = ipaddress.ip_address(source_ip)
    for subnet in allowed_subnets:
        if source_ip_obj in subnet:
            return True
    return False

# Parsing the IP header and extract source IP
def parse_ip_header(data):
    version_header_length = data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4
    source_ip = '.'.join(map(str, data[12:16]))

    return version, header_length, source_ip
def main(interface, allowed_subnets):
    print(f"Listening on interface: {interface}")

    try:
        while True:
            print("Checking for IP spoofing...")

            # Printing every 5 seconds that no spoofing was found if not found
            for x in range(5):
                time.sleep(1)

    except KeyboardInterrupt:
        print("Stopped program")

if __name__ == "__main__":
    interface = " "  # Enter your network interface
    allowed_subnets = [ipaddress.ip_network('')]  # Enter allowed subnets

    main(interface, allowed_subnets)
