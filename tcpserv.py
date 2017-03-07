from socketserver import BaseRequestHandler, TCPServer
class EchoHandler(BaseRequestHandler):

    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            print("Received at server end {0}".format(msg))
            self.request.send(msg)
if __name__ == '__main__':
    serv = TCPServer(('', 2000), EchoHandler)
    serv.serve_forever()