#!/usr/bin/env python3

import socket 
import re 

def check_domain(domain):
    if re.match(r'^[a-zA-Z0-9.-]+$', domain): 
        return domain

def check_port(port):
    return port.isdigit() and int(port) >= 0 and int(port) <= 1000 

def scan_port(domain, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.settimeout(1)

        result = s.connect_ex((domain, port)) 
        s.close()
        
        if result == 0: 
            return "open"
        else: 
            return "closed"
        
    except Exception as e: 
        return e

def main():
    print("Welcome to PortPinger.") 
    print("Type '--help or --h' for help, or '--version or --v' for version.") 
    
    while True: 
        target_domain = input("Enter the domain/IPv4: ") 
        
        if target_domain in ['--help', '--h']: 
            print("Help: This script scans ports of a given domain.")           
            print("Step 1. Enter the target domain or IP address. Ex: google.com or 8.8.8.8")
            print("Step 2. Enter the first port number you would like to scan. Ex: 443")
            print("Step 3. Enter the last port number you would like to scan. Ex: 759")
            print("Note. The program scans all specified ports, and those in between.")
            continue
           
        if target_domain in ['--version', '--v']: 
            print("PortPinger v1.0")
            continue
            
        if not check_domain(target_domain): 
            print("Invalid domain format. Please enter a valid domain.")
            continue
        break

    
    while True: 
        start_port = input("Enter a starting port between 0 and 1000: ") 
        if not check_port(start_port): 
            print("Invalid port. Please enter a valid port.")
            continue
        
        end_port = input("Enter an ending port between {} and 1000: ".format(start_port))
        if not check_port(end_port): 
            print("Invalid port. Please enter a valid port.")
            continue
        
        if int(end_port) < int(start_port): 
            print("Ending port must be greater than or equal to starting port.")
            continue
        break
    
    print("Scanning ports...\n") 
    for port in range(int(start_port), int(end_port)+1): 
        port_status = scan_port(target_domain, port) 
        if port_status == "open": 
            print(f"\033[92m{target_domain} Port {port}: {port_status}") 
        elif port_status == "closed":
            print(f"\033[91m{target_domain} Port {port}: {port_status}") 
        else:
            print(f"\033[93m{target_domain} Port {port}: {port_status}") 

if __name__ == "__main__": 
    main()