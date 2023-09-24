# IP_Anti_Spoofing
# This program is used to capture network frames on a specific interface and monitor the source IP addresses to detect potential IP spoofing attempts in network traffic. If such an attempt is detected, the program will display a message about suspected spoofing

# The source_ip_test function accepts a source IP address and a list of allowed subnets. Checks whether the IP address is in one of the allowed subnets and returns True if so, or False if not. 

# The main function initiates frame capture on a specific interface. Displays information about listening on a given interface. For each captured frame, it parses the IP header to obtain the source IP address ,calls the source_ip_test function to check whether the source IP address is in one of the allowed subnets. If the IP address is not in any of the allowed subnets, it displays a message.
