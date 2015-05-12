from twisted.internet.protocol import ServerFactory
from twisted.python import log
from MainProtocol import MainProtocol

class MainFactory(ServerFactory):

	protocol = MainProtocol

	def startFactory(self): pass

	def stopFactory(self): pass