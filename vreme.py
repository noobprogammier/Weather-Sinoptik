from vremeto import *
from logging import info as inf, warning as warn, error as err, DEBUG, basicConfig
class CheckSNVR(object):
	def __init__(self, region:list, output:str, warnings:str, weathermore:bool) -> str:
		cases_ = {"html":("html_dualpart"), "plain":("text"), "json":("json")}[output]
		self.mashup = {"parts":cases_, "regions":region}
		self.stript = True
		self.return_ogdoc = True
		self.verbosity = False
		self.warnings = warnings
		self.weathermore = weathermore
	@property
	def getrs(self):
		alls_ = {}
		og = {}
		warnings = self.warnings
		if self.verbosity == True:
			warn("Getting information, about all regions specified (%d)"%(len(self.mashup["regions"],)))
		if len(self.mashup["regions"]) >= 3:
			if warnings == "strict":
				warn("We recommend the 'requests' to be not bigger than 2! You provided '%d'."%(len(self.mashup["regions"])))
		for items in self.mashup["regions"]:
			if items not in oblasti:
				if warnings == "strict":
					err("%s not found!"%(items))
			else:
				pans, html_doc = get_weather(items, self.weathermore).getw()
				alls_[items] = pans
				og[items] = html_doc
		if self.verbosity == True:
			warn("Loaded %d information (OG information: %d). . ."%(len(alls_), len(og)))
		temp = {}
		if self.verbosity == True:
			warn("Preparing to make strings with %s format. . . ."%(self.mashup["parts"]))
		if self.mashup["parts"] == "json":
			"""
If the specified format is json."""
			return alls_
		if self.mashup["parts"] == "html_dualpart":
			"""
If the specified format is HTML. """
			for items in alls_:
				"""
The actual formation .. . """
				temp[items] = '''
<!DOCTYPE html PUBLIC>
<html lang="en">
<head>
<title> Vremeto - %s </title>
</head>'''%(items)
		else:
			final = []
			for items in alls_:
				trash =  [ir for ir in alls_[items]]
				final.append(f"{items} >> \r\x0A\r\x0A" + "".join(alls_[items][item] for item in trash))
		if self.mashup["parts"] == "html_dualpart":
			if self.verbosity == True:
				warn("Loading it as a html plate object. . . ")
			final = []
			for iterx in temp:
				main_item = alls_[iterx][0]
				final.append(temp[iterx] + "<br><body> <span> <p> %s </p> </span> </body> </html>"%("<br>".join("%s || %s: %s "%(iterx,cry, main_item[cry]) for cry in main_item)))
		if self.stript == True:
			if self.verbosity == True:
				warn("Stripping the text. . ..")
			temp = []
			for items in range(len(final)):
				temp.append(final[items].strip())
			final = temp
		else:
			pass
		if self.verbosity == True:
			warn("Argument is %s for original document . . . ."%(self.return_ogdoc))
		if self.return_ogdoc == True:
			"""
If it's True"""
			ogs = []
			for items in og:
				ogs.append(og[items])
			if self.verbosity == True:
				warn("Total loaded %d"%(len(ogs,)))
			return final, ogs
		if self.verbosity == True:
			warn("Returning. . . .")
		return final
	@getrs.setter
	def verbose(self, vl:bool) -> bool:
		if type(vl) != bool:
			raise exc(error_tab["TypeError"]%("bool", type(vl)))
		self.verbosity = vl
	@getrs.setter
	def rnm(self, vl:bool):
		self.stript = vl
	@getrs.setter
	def ogdoc(self, vl:bool):
		if isinstance(vl, bool) != True:
			raise exc(error_tab["TypeError"]%("bool", type(vl)))
		self.return_ogdoc = vl