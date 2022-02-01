from argparse import ArgumentParser
from vremeto import *
class App():
	def __init__(self):
		parsefc = ArgumentParser(description='''
A command-line for Weather-Sinoptik.\r\x0A''')
		parsefc.add_argument("-ts", "--target", help="Provide an argument, a city.", required=True)
		parsefc.add_argument("-gui", "--graphicalinterface", help="This option is for the GUI, which GUI can be set to be True or False.", default=False, required=False)
		if parsefc.parse_args().target == "show":
			print("Existing locations (%d)>> \r\x0A\r\x0A"%(len(oblasti)) + "\x0A".join(bob for bob in oblasti))
			exit()
		if parsefc.parse_args().target not in oblasti:
			raise exc(error_tab["Missing"]%(parsefc.parse_args().target))
		self.setted = {"target":parsefc.parse_args().target, "gui":parsefc.parse_args().graphicalinterface}
	@property
	def build(self):
		get_, htmldoc = get_weather(oblast=self.setted["target"]).getw()
		return get_, self.setted
if __name__ == "__main__":
	app, setobject = App().build
	if setobject["gui"] == "True":
		displaygraph(param="".join(app[itemx] for itemx in app))
	else:
		print("".join(app[itemx] for itemx in app))

