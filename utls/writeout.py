from json import dumps
def writeOutPut(file_name:str, objectrel:dict) -> str:
	with open(file_name, "w", encoding="utf-8") as file:
		file.write(dumps(objectrel))
	file.close()
