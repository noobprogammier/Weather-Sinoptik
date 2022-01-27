from vremeto import * 
from os import system
def mainprogram():
	locations = {"1":"Shumen", "2":"Varna"}
	while True:
		print("\r\x0A\r\x0AAvailiable locations::\r\x0A\r\x0A" + "\x0A".join("%s.\x20"%(bob) + locations[bob] for bob in locations))
		strs = str(input("> "))
		if strs not in locations:
			raise exc(error_tab["Missing"]%(strs))
		get_ = get_weather(oblast=locations[strs]).getw()
		print(">>> \r\x0A%s <<<"%(("\x2D"*40 + "\r\x0A").join("%s \r\x0A\r\x0A"%(bob) + get_[bob] for bob in get_)))
		input("\r\x0A\r\x0APress any button to continue. . . . . .\r\x0A")
		system("cls")
if __name__ == "__main__":
	mainprogram()