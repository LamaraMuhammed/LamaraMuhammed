# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


from twisted.web import server, resource
from twisted.internet import protocol, reactor, endpoints


class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""

    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        print(data)
        self.transport.write(b"from serv: \n" + data)


def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.isLeaf = True
    def render():
        return "jksdakf"
    factory.protocol = Echo
    site = server.Site(factory)
    endpoint = endpoints.TCP4ServerEndpoint(reactor, 8000)
    endpoint.listen(site)
    # reactor.listenTCP(8000, factory)
    reactor.run()


# this only runs if the module was *not* imported
if __name__ == "__main__":
    main()
