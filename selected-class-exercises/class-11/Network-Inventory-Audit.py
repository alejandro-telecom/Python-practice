# Exercise of Class 11 — Network Inventory Audit

# Device inventory
# (hostname, management_ip, location, vlans)

inventory = [
    ("R1", "192.168.1.1", "HQ", (10, 20, 30)),
    ("SW1", "192.168.1.2", "HQ", (10, 20, 40, 40)),
    ("SW2", "192.168.1.2", "Branch", (10, 50, 99)),
    ("R2", "192.168.1.4", "Branch", (10, 20, 50)),
    ("SW3", "192.168.1.5", "HQ", (10, 30, 60))
]

# Approved VLANs in the infrastructure
approved_vlans = {10, 20, 30, 40, 50}

# VLANs that must be present on all devices
required_vlans = {10, 20}

# Variables to use
total_devices = 0
ip_list = []
duplicate_ips = set()
seen_ips = set()
duplicate_ip_devices = []

# Loop through the inventory
for hostname, management_ip, location, vlans in inventory:
    total_devices += 1
    ip_list.append(management_ip)

# Checking for repeated IPs and, if any, finding out which ones:
for ip in ip_list:
    if ip in seen_ips:
        duplicate_ips.add(ip)
    else:
        seen_ips.add(ip)

# Names of devices that have duplicate IPs associated with that IP
for duplicated in duplicate_ips:
    for hostname, management_ip, location, vlans in inventory:
        if duplicated == management_ip:
            duplicate_ip_devices.append((hostname, duplicated))

print('\t\t\tREPORT')
print(f"\nTotal devices: {total_devices}")

print('\nIP')
print(f'-There are {len(set(ip_list))} IP addresses:')
for ip in set(ip_list):
    print(f"\t{ip}")
print(f"-There are {len(seen_ips) - len(duplicate_ips)} non-duplicated IPs.")

if len(duplicate_ips) > 0:
    print(f"\r-Duplicate IPs: {duplicate_ips}")
    print("-Duplicate relationship (hostname, ip):")
    for hostname, ip in duplicate_ip_devices:
        print(f"\t{hostname}, {ip}")
else:
    print(f"\r-There are no duplicate IPs")