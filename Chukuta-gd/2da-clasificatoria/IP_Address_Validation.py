# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

ipv4 = r'^(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$'
ipv6 = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'


for _ in range(int(input())):
    string = input()
    if re.findall(ipv4, string):
        print('IPv4')
    elif re.findall(ipv6, string):
        print('IPv6')
    else:
        print('Neither')