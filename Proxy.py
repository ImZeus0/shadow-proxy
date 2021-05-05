import subprocess

class Proxy():

    def __init__(self,ip,port,internal_port):
        self.internal_port = internal_port
        self.ip = ip
        self.port = port

    def print_info(self):
        print(self.ip,self.port,self.internal_port)

    def is_online(self):
        try:
            address = self.ip+":"+self.port
            data = subprocess.check_output(['curl', '-m', '2', '--socks5', address, "http://ifconfig.co/json"])
            return True
        except:
            return False

