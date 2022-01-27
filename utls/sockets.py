from socket import socket, AF_INET, SOCK_STREAM, getprotobyname
class make_socket(object):
	def __init__(self, buffer:int) -> int:
		sock = socket(AF_INET, SOCK_STREAM, getprotobyname("tcp"))
		sock.connect(("www.sinoptik.bg", 443))
		self.socket = sock
	@property
	def getfsock(self):
		return self.socket
	@getfsock.setter
	def maken(self, nsock):
		self.socket = nsock