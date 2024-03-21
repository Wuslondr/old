# l = []
# c = 0
# from ipaddress import *
# for a in range(256):
#     io = ip_address(f"246.81.65.{a}")
#     net = ip_network(f"{io}/255.255.255.224", 0)
#     if io not in (net.network_address, net.broadcast_address):
#         if all([bin(int(ip))[2:][16:24].count("0")> bin(int(ip))[2:][24:].count("0") for ip in net.hosts()]):
#             l.append(a)
# print(len(l))


# from ipaddress import *
# from fnmatch import *
# ip = ip_address('152.65.245.132')
# for mask in range(33):
#    network = ip_network(f'{ip}/{mask}', 0)
#    if fnmatch(str(network.netmask), '255.255.*.0'):
#         if all(bin(int(ip))[2:][:16].count("0")>= bin(int(ip))[2:][16:].count("0")
#             for ip in network):
#             print(network.netmask)
