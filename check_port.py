import subprocess
import re
from Proxy import Proxy


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
            res_list.append(Proxy(params[1],params[2],params[0][:-2]))
            return res_list

def get_internal_ports():
    res_list = []
    proxys = get_list_enable_proxy()
    for proxy in proxys:
        res_list.append(proxy.internal_port)
    return res_list




if __name__ == "__main__":
    print(get_internal_ports())