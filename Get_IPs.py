#!/usr/bin/python3
import ipaddress
import re
import sys


def validate_ip_address(address):
    try:
        ipaddress.IPv4Address(address)
        #print(f"IP address {address} is valid.")
        return True
    except Exception:
        #print(f"IP address {address} is not valid")
        return False


f = open(sys.argv[1],'r')
text = f.read()

bad_ips = []
ips = [] 
regex = re.findall(r'(?:[^.])(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',text)
if regex is not None:
    for match in regex:
        if match not in ips:
            if validate_ip_address(match):
                ips.append(match)
            else:
                bad_ips.append(match)

print("Valid IPs:")
print(ips)
print("Invalid IPs:")
print(bad_ips)

out_file = open('./validated_ips.txt', 'w')
for ip in ips:
    out_file.write(ip)
    out_file.write('\n')
out_file.close()




