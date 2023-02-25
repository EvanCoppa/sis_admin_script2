#!/usr/bin/env python3
# Evan Coppa 02/17/2023

import socket
import os
import datetime



os.system('clear')

# Get the current date
current_date = datetime.date.today()

# Print the current date


# Get network interface and mask
ni_if = os.net_if_stats()
ni_addr = os.net_if_addrs()
net_info = []
for iface in ni_addr:
    if iface.startswith('lo'):
        continue
    net_mask = ni_addr[iface][0].netmask
    net_info.append((iface, net_mask))

# Get primary and secondary DNS servers
with open('/etc/resolv.conf', 'r') as f:
    resolv_conf = f.readlines()
    nameservers = [line.split()[1] for line in resolv_conf if line.startswith('nameserver')]

# Get operating system, operating system version, and kernel version
os_info = os.uname()

# Get hostname and domain
hostname = socket.gethostname()
domain = socket.getfqdn().split('.', 1)[1]

# Get system disk size and available space
disk_info = psutil.disk_usage('/')

# Get CPU information
cpu_info = []
for i, cpu in enumerate(psutil.cpu_freq(percpu=True)):
    cpu_info.append(('CPU {}'.format(i+1), cpu.current))

# Get number of CPUs and CPU cores
num_cpus = psutil.cpu_count()
num_cores = psutil.cpu_count(logical=False)

# Get total and available RAM
mem_info = psutil.virtual_memory()

# Print system information
print("Current date: ", current_date)
print('Network Interface and Mask:')
for iface, mask in net_info:
    print('\tInterface: {}, Mask: {}'.format(iface, mask))
print('\nPrimary and Secondary DNS Servers:')
for ns in nameservers:
    print('\t{}'.format(ns))
print('\nOperating System Information:')
print('\tOS: {}, Version: {}, Kernel: {}'.format(os_info.system, os_info.release, os_info.version))
print('\nHostname Information:')
print('\tHostname: {}, Domain: {}'.format(hostname, domain))
print('\nDisk Information:')
print('\tSize: {:.2f} GB, Available: {:.2f} GB'.format(disk_info.total/(1024**3), disk_info.free/(1024**3)))
print('\nCPU Information:')
for cpu, freq in cpu_info:
    print('\t{}: {} MHz'.format(cpu, freq))
print('\nNumber of CPUs: {}, Number of CPU Cores: {}'.format(num_cpus, num_cores))
print('\nMemory Information:')
print('\tTotal: {:.2f} GB, Available: {:.2f} GB'.format(mem_info.total/(1024**3), mem_info.available/(1024**3)))
