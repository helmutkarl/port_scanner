import socket
from datetime import datetime

def scan_port(ip, port):
    # establish TCP connection
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.1) # move on to next port after 100ms

    try:
        # connect to given IP and port
        result = scanner.connect_ex((ip, port))
        if result == 0:
            scanner.close()
            return 0
    except socket.error:
        print(f"Could not connect to {ip}")
    scanner.close()
    return 1
    
def scan_ports(target_ip, start_port, end_port):
    print(f"Scanning {target_ip} from port {start_port} to {end_port}")
    start_time = datetime.now()
    open_ports = []

    for port in range(start_port, end_port):
        if scan_port(target_ip, port) == 0:
            open_ports.append(port)

    end_time = datetime.now()
    duration = end_time - start_time

    # print results
    print(f"Scanning completed in {duration}.\n The following ports are open:")
    for open_port in open_ports:
        print(open_port)

if __name__ == "__main__":
    # Take target IP and port range input from the user
    target_ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    scan_ports(target_ip, start_port, end_port)