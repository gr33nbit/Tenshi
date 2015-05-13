import optparse
from twisted.internet import reactor, ssl
from twisted.internet.endpoints import SSL4ClientEndpoint
from OpenSSL.SSL import TLSv1_METHOD
from inc.MainFactory import MainFactory


def parse_options():

	usage = """usage: %prog [options] host port cert privkey"""
	
	parser = optparse.OptionParser(usage)
	_, args = parser.parse_args()

	if len(args) != 4:
		parser.error("wronge number of arguments")

	else:
		return args

(host, port, cert, privKey) = parse_options()

port = int(port)

sslContextFactory = ssl.DefaultOpenSSLContextFactory(privKey, cert, sslmethod=TLSv1_METHOD)
#ClientEndpoint = SSL4ClientEndpoint(reactor, host, 12345, sslContextFactory, 30, (host, port))

connector = reactor.connectSSL(host, port, MainFactory(), sslContextFactory, 30, None)

reactor.run()