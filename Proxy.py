

class Proxy():

    def __init__(self,ip,port,internal_port):
        self.internal_port = internal_port
        self.ip = ip
        self.port = port

    def print_info(self):
        print(self.ip,self.port)


p = Proxy('10.10.10.10',555)
p.print_info()