from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory
from MainProtocol import MainProtocol

class MainFactory(ClientFactory):

	protocol = MainProtocol

	def startFactory(self): pass


	def stopFactory(self):
		
		reactor.stop()
		print 'stoped'
		

	def clientConnectionFailed(self, connector, reason):

		print reason


