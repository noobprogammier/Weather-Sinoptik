from utls.sockets import *
from utls.pyssl import * 
from utls.errors import * 
from utls.oblasti import *
from utls.payloads import *
from utls.bs import *
from utls.writeout import *
from utls.gui import * 
class get_weather(object):
	def __init__(self, oblast:str, weathermore:bool) -> str:
		capital = (oblast[0].upper() + oblast[1:])
		if capital not in oblasti:
			raise exc(error_tab["Missing"]%(capital))
		location = oblasti[capital]
		socks = []
		for times in range(2):
			god = make_socket(buffer=4096)
			god.maken = make_socket(buffer=4096).getfsock
			socks.append(god.getfsock)
		data = {}
		sex = [("weather", socks[0]), ("www", socks[1])]
		ready = [make_socket_ssl(socket={"sock":(sex[_][1]), "host":"%s.sinoptik.bg"%(sex[_][0])}) for _ in range(2)]
		data["www"] = send_GET(sock={"location":location, "host":"www.sinoptik.bg", "sock":ready[1]})
		if weathermore == True:
			data["weather"] = send_GET(sock={"location":"widget/%s/1/728/90/1?url=https://weather.sinoptik.bg/widgets"%(location.split("-")[2]), "host":"weather.sinoptik.bg", "sock":ready[0]})
		forecast_decoded_HTML = {}
		try:
			for items in data:
				try:
					forecast_decoded_HTML[items] = data[items].decode("utf-8", errors="ignore")
				except UnicodeDecodeError:
					forecast_decoded_HTML[items] = data[items].decode("ISO-8859-1", errors="ignore")
		except KeyboardInterrupt as fail:
			print("\r\x0A[DATA] Try again later. . . .")
			data = "none"
		self.lean = weathermore
		if weathermore == True:
			self.partidata = [getWeather(data=forecast_decoded_HTML["www"], weather=False)[0], getWeather(data=forecast_decoded_HTML["weather"], weather=True)[0]]
		else:
			self.partidata = [getWeather(data=forecast_decoded_HTML["www"], weather=False)[0]]
		if weathermore == True:
			self.html_doc_1, self.html_doc_2 = getWeather(data=forecast_decoded_HTML["www"], weather=False)[1], getWeather(data=forecast_decoded_HTML["weather"], weather=True)[0]
		else:
			self.html_doc_1 = getWeather(data=forecast_decoded_HTML["www"], weather=False)[1]
	def getw(self):
		if self.lean == True:
			return self.partidata, (self.html_doc_1, self.html_doc_2)
		else:
			return self.partidata, self.html_doc_1


