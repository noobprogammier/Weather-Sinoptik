from bs4 import BeautifulSoup
def getWeather(data:str) -> str:
	real_data = data.split("\r\x0A\r\x0A")[1]
	items = [val for val in [bob for bob in real_data.split("\x0A") if '<meta name="description"' in bob][0].split("=")[2]]
	gather = "".join(bob for bob in items).split(">")[0].replace('"', "").replace("/", "")
	rep = BeautifulSoup(data, "html.parser")
	days = [bob.get_text() for bob in rep.find_all("span",{"class":"wfNonCurrentDay"})]
	curr = [bob.get_text() for bob in rep.find_all("span",{"wfNonCurrentTemp"})]
	other_data = [bob.get_text() for bob in rep.find_all("span", {"class":"wfNonCurrentValue"})]
	signature = {}
	count = 0
	update = {}
	for items in curr:
		signature[days[count]] = "Minimal temperature: %s"%(items.split("|")[0].strip()) + "\r\x0AMaximum temperature: %s"%(items.split("|")[1].strip())
		count += 1
	cases = {}
	bob = 0
	whole = ""
	red = 0
	for times in range(3):
		for items in range(9):
			whole += other_data[red] + "\r\x0A"
			red += 1
		whole += "|"
		bob += 1
	count = 0
	maked = [item for item in whole.split("|")]
	for items in signature:
		update[items] = signature[items] + maked[count]
		count +- 1
	return update
