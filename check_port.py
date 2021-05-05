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
    new_port = 0
    while True:
        new_port = random.randint(500,65000)
        if new_port in internal_ports:
            continue
        else:
            break
    command = f'iptables -t nat -A PREROUTING -p tcp --dport {new_port} -j DNAT --to-destination {ip}:{port}'
    res = os.system(command)
    if res == 0:
        return new_port
    else:
        return 1

def delete_offline():
    proxys = get_list_enable_proxy()
    i = 0
    while i < len(proxys):
        if proxys[i].is_online()==False:
            print('delete '+str(i))
            os.system('iptables -t nat -D PREROUTING '+str(i+1))
        i+=1
    print('end')



if __name__ == "__main__":
    num = input("1. create rule\n2. list rule\n-> ")
    if num == '1':
        port = input('port ')
        ip = input('ip ')
        res = create_new_rule(ip,port)
        if res == 0:
            print('+')
        else:
            print('error')
    elif num == '2':
        rules = get_list_enable_proxy()
        for rule in rules:
            print(f'internal port: {rule.internal_port} ip: {rule.ip} port {rule.port}\n')
    elif num == '3':
        delete_offline()