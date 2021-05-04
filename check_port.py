import subprocess
data = subprocess.check_output(['iptables','-t','nat','-L','--line-numbers','-n'])
data = data.decode('utf-8')
lines_data = data.split('\n')
for line in lines_data:
    if 'dpt' in line:
        print(line)
