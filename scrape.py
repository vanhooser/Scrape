import dryscrape, time, json
from bs4 import BeautifulSoup


skipToTH = False
skipToTD = False

tdskip = 0

title = ""
time = ""
days = ""
location = ""
with open('output.txt', 'a') as f:
	for line in open('class.html', 'r').readlines():
		soup = BeautifulSoup(line)

		for p in soup.find_all('td'):
			if not skipToTH:
				if tdskip > 0:
					try:
						if(str(p.string) and len(str(p.string.strip())) != 0):
							if tdskip == 0:
								tdskip += 1
								continue
							if tdskip == 1:
								
								tdskip += 1
								continue
							elif tdskip == 2:
								time = p.string
								tdskip += 1
								continue
							elif tdskip == 3:
								days = p.string
								tdskip += 1
								continue 
							elif tdskip == 4:
								location += p.string
								tdskip += 1
								continue
							else:
								skipToTH = True
								skipToTD = False
								out = json.dumps({"title": title,
									"time" : time,
									"days" : days,
									"location" : location
									})
								print out
								f.write(out + '\n')
					except:
						continue
				else:
					tdskip += 1
					continue

		for p in soup.find_all('th'):
			"""
			if(thskip == 1):
				continue
				"""
			if not skipToTD:
				try:
					title = p.string.split(" - ")
					skipToTD = True
					skipToTH = False
					#tdskip = 0
				except:
					continue