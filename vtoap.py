from vremeto import * 
from os import system
def mainprogram(gui:bool) -> dict:
	locations = {"Bulgaria":{"1":"Shumen", "2":"Varna", "3":"Sofia", "4":"Plovdiv", "5":"Ruse", "6":"Stara Zagora", "7":"Vidin"}}
	while True:
		if type(gui) != bool:
			raise exc(error_tab["TypeError"]%("bool", type(gui)))
		print("Availiable locations (%s)>> \r\x0A\r\x0A"%(len(locations)) + "%s"%("\x0A".join(bob for bob in locations)))
		strs = str(input(">> "))
		if len(strs) == 0 or strs not in locations:
			raise exc(error_tab["Missing"]%(strs))
		preorder = ",".join(bob for bob in locations[strs])
		print("\r\x0AAvailiable locations for %s (%s)>> \r\x0A"%(strs, len(locations[strs])) + "\x0A".join("%s. %s"%(six, locations[strs][six]) for six in preorder.split(",")))
		locs = str(input(">> "))
		if len(locs) == 0 or locs not in locations[strs]:
			raise exc(error_tab["Missing"]%(locs))
		after_all, html_doc = get_weather(oblast=locations[strs][locs]).getw()
		output_ = writeOutPut(file_name="%s_%s.js"%(strs+"-"+locations[strs][locs], len(after_all)), objectrel=after_all)
		if gui == [False, True][1]:
			displaygraph("Weather >> \r\x0A" + "".join("%s: %s"%(bob, after_all[bob]) for bob in after_all))
			exit()
		print("Weather >> \r\x0A" + "".join("%s: %s"%(bob, after_all[bob]) for bob in after_all))
		input("\r\x0A\r\x0A Press any key \r\x0A")
		system("cls")
if __name__ == "__main__":
	mainprogram(gui=False)