from utls.sockets import *
from utls.pyssl import * 
from utls.errors import * 
from utls.oblasti import *
from utls.payloads import *
from utls.bs import *
from utls.writeout import * 
class get_weather(object):
	def __init__(self, oblast:str) -> str:
		capital = (oblast[0].upper() + oblast[1:])
		if capital not in oblasti:
			raise exc(error_tab["Missing"]%(capital))
		location = oblasti[capital]
		god = make_socket(buffer=4096)
		god.maken = make_socket(buffer=4096).getfsock
		final = god.getfsock
		ready = make_socket_ssl(socket={"sock":final, "host":"www.sinoptik.bg"})
		data = send_GET(sock={"location":location, "host":"www.sinoptik.bg", "sock":ready})
		try:
			data = data.decode("utf-8", errors="ignore")
		except UnicodeDecodeError:
			data = data.decode("ISO-8859-1")
		except KeyboardInterrupt as fail:
			print("\r\x0A[DATA] Try again later. . . .")
			data = "none"
		self.final = getWeather(data=data)
	def getw(self):
		return self.final


