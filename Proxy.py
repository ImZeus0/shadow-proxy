

class Proxy():

    def __init__(self,ip,port,internal_port):
        self.internal_port = internal_port
        self.ip = ip
        self.port = port

    def print_info(self):
        print(self.ip,self.port,self.internal_port)

