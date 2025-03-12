from get_interface import choose_interface_and_get_info
import scapy.all as scapy
import termcolor

my_machine = choose_interface_and_get_info()

def find_range(ip):
    octets = ip.split(".")
    octets.pop(len(octets) - 1)
    octets.append("1/24")
    new_ip = '.'.join(octets)
    return new_ip
    

def show_contents_in_manner(list_of_answered_packets):
    print("----IP---------------MAC------------")
    for sent, received in list_of_answered_packets:
        print(f"{received.psrc}\t\t{received.src}")


def scan(ip, my_ip, my_mac):
    arp_packet = scapy.ARP(pdst=ip, psrc=my_ip, hwsrc=my_mac)
    broadcast_packet = scapy.Ether(src=my_mac, dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet / arp_packet
    answered = scapy.srp(combined_packet, timeout=1, verbose=False)[0]
    show_contents_in_manner(answered)



print(termcolor.colored('[-] If you do not get result try to check interface you selected or select interface which is connected to internet', 'red'))

if my_machine is not None:
    scan(find_range(my_machine['ip']), my_machine['ip'], my_machine['mac'])
else:
    print("[-] Please Check the Right Interface that has valid IP")
    exit()


