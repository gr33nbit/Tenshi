from imports.PithosService import PithosService
from imports.PithosFactory import PithosFactory
from twisted.application import internet, service

port = 12021
iface = 'localhost'

top_service = service.MultiService()


Pithos_Service = PithosService()
Pithos_Service.setServiceParent(top_service)

factory = PithosFactory(Pithos_Service)
tcp_service = internet.TCPServer(port, factory, interface=iface)
tcp_service.setServiceParent(top_service)

application = service.Application("Pithos")

top_service.setServiceParent(application)
