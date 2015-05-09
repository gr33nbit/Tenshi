from twisted.internet import defer, reactor
from twisted.internet.protocol import ServerFactory, Protocol
from twisted.python import log

class PithosProtocol(Protocol):

	def __init__(self):

		pass

	def connectionMade(self):
		pass

class PithosFactory(ServerFactory):

	protocol = PithosProtocol

	def __init__(self, service):

		self.service = service
