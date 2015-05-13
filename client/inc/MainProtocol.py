from twisted.internet.protocol import Protocol
from  twisted.internet import reactor


class MainProtocol(Protocol):

	def connectionMade(self):

		self.transport.write('HELLO :D hehe')

	def dataReceived(self, data):

		print data

	def connectionLost(self, reason):

		print reason

