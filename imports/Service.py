from twisted.application import service
from twisted.internet import defer, reactor
from twisted.python import log

class PithosService(service.Service):
	
	def __init__(self):

		pass

	def startService(self):

		service.Service.StartService(self)
