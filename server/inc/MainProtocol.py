from twisted.internet.protocol import Protocol


class MainProtocol(Protocol):


	def connectionMade(self):

		self.transport.write('welcome to the serveratron 3000 mtfcker\r\n')

	def connectionLost(self):
		pass

	def dataReceived(self, data):

		print data

		self.transport.write(data+'\r\n')
		self.transport.loseConnection()