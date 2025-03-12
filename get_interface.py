import socket
import termcolor
import psutil


def get_ip(interface_name):
    # Function to get the IP address associated with a given network interface
    interface = psutil.net_if_addrs().get(interface_name)
    for each_address in interface:
        if each_address.family == socket.AF_INET:
            # If the address matches INET(IPV4) address return it
            return each_address.address


def get_mac(interface_name):
    interface = psutil.net_if_addrs().get(interface_name)
    for each_address in interface:
        if each_address.family == psutil.AF_LINK:
            # IF the layer matches AF_LINK(MAC) return it with replaced values of :
            return (each_address.address).replace("-", ":")

def choose_interface_and_get_info():
    # Function to choose a network interface and retrieve its information
    all_interfaces = psutil.net_if_addrs()
    list_of_interfaces = []
    for interfaces, address in all_interfaces.items():
        list_of_interfaces.append(interfaces)

    # Display interfaces with its choices
    print(termcolor.colored(f"[+] Choose from the list of Interfaces to scan", "green"))
    for interface_number in range(len(list_of_interfaces)):
        # Display the available network interfaces and their corresponding numbers
        print(f"For {list_of_interfaces[interface_number]}, Enter: {interface_number + 1}")
    print("\n\n")
    choice = int(input(termcolor.colored(f"[+] Enter Your Choice: ", "yellow")))  # User selects a network interface
    try:
        return {
            'Interface': list_of_interfaces[choice - 1],  # Return the selected interface name
            'ip': get_ip(list_of_interfaces[choice - 1]), # Return the IP address of the selected interface
            'mac': get_mac(list_of_interfaces[choice - 1])
        }
    except:
        print("[-] Please Enter the Valid Choice")
        return None


