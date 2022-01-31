from vremeto import * 
from os import system
def mainprogram():
	locations = {"Bulgaria":{"1":"Shumen", "2":"Varna", "3":"Sofia"}}
	while True:
		print("Availiable locations>> \r\x0A\r\x0A" + "%s"%("\x0A".join(bob for bob in locations)))
		strs = str(input(">> "))
		if len(strs) == 0 or strs not in locations:
			raise exc(error_tab["Missing"]%(strs))
		preorder = ",".join(bob for bob in locations[strs])
		print("\r\x0AAvailiable locations for %s>> \r\x0A"%(strs) + "\x0A".join("%s. %s"%(six, locations[strs][six]) for six in preorder.split(",")))
		locs = str(input(">> "))
		if len(locs) == 0 or locs not in locations[strs]:
			raise exc(error_tab["Missing"]%(locs))
		after_all = get_weather(oblast=locations[strs][locs]).getw()
		output_ = writeOutPut(file_name="%s_%s.js"%(strs+"-"+locations[strs][locs], len(after_all)), objectrel=after_all)
		print("Weather >> \r\x0A" + "".join("%s: %s"%(bob, after_all[bob]) for bob in after_all))
if __name__ == "__main__":
	mainprogram()