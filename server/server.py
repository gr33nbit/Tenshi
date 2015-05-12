from inc.MainFactory import MainFactory
from twisted.internet.protocol import ServerFactory
from twisted.application import internet, service, strports
from twisted.internet import endpoints, reactor
 
port = 12021
iface = 'localhost'
 
server_string = "ssl:interface=%(interface)s:port=%(port)s:privateKey=%(cert)s:sslmethod=%(sslmethod)s"
server_dict = {'port': port, 'interface': iface, 'cert': './certs/server.pem', 'sslmethod': 'TLSv1_METHOD'}
sslsvc = strports.service(server_string % server_dict, MainFactory())

application = service.Application("Tenshi")
serviceCollection = service.IServiceCollection(application)
sslsvc.setServiceParent(serviceCollection)

