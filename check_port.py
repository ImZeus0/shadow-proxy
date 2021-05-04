import subprocess
import re
from Proxy import Proxy
import random
import os


def search_ip_port(line):
    pattern = r'\d{1,5} to:\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,5}'
    result = re.search(pattern, line)
    return result.group(0)

def get_list_enable_proxy():
    res_list = []
    data = subprocess.check_output(['iptables', '-t', 'nat', '-L', '--line-numbers', '-n'])
    data = data.decode('utf-8')
    lines_data = data.split('\n')
    for line in lines_data:
        if 'dpt' in line:
            line = search_ip_port(line)
            params = line.split(':')
            res_list.append(Proxy(params[1],params[2],int(params[0][:-3])))
            return res_list

def get_internal_ports():
    res_list = []
    proxys = get_list_enable_proxy()
    for proxy in proxys:
        res_list.append(proxy.internal_port)
    return res_list

def create_new_rule(ip,port):
    internal_ports = get_internal_ports()
    new_port = random.randint(500,65000)
    if new_port in internal_ports:
        print("port X")
    else:
        command = f'iptables -t nat -A PREROUTING -p tcp --dport {new_port} -j DNAT --to-destination {ip}:{port}'
        print(command)




if __name__ == "__main__":
    create_new_rule('99.99.99.99','7777')