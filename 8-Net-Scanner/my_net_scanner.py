from socket import timeout
import scapy.all as scapy

# 1- Arp Request
# 2- Broadcast
# 3- Response


arp_request_packet = scapy.ARP(pdst="192.168.218.0/24")
#scapy.ls(scapy.ARP())
broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#scapy.ls(scapy.Ether())
combined_packet = broadcast_packet / arp_request_packet
(answered_list , unanswered_list ) = scapy.srp(combined_packet,timeout=1)
#print(list(answered_list))

answered_list.summary()