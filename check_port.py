import subprocess
import re


def search_ip_port(line):
    pattern = r'\d{1,5} to:\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,5}'
    result = re.search(pattern, line)
    print(result.group(0))

def get_list_enable_proxy():
    data = subprocess.check_output(['iptables', '-t', 'nat', '-L', '--line-numbers', '-n'])
    data = data.decode('utf-8')
    lines_data = data.split('\n')
    for line in lines_data:
        if 'dpt' in line:
            search_ip_port(line)



if __name__ == "__main__":
    get_list_enable_proxy()