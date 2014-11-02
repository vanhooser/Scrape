import dryscrape, requests, json
from bs4 import BeautifulSoup

url = "https://coursecatalog.harvard.edu/icb/icb.do?keyword=CourseCatalog&panel=icb.pagecontent695860%3Arsearch%3Ffq_coordinated_semester_yr%3D%26fq_school_nm%3D%26q%3D%26sort%3Dcourse_title%2Basc%26start%3D0%26submit%3DSearch&pageid=icb.page335057&pageContentId=icb.pagecontent695860&view=search&viewParam_fq_coordinated_semester_yr=&viewParam_fq_school_nm=&viewParam_q=&viewParam_sort=course_title+asc&viewParam_start={0}&viewParam_submit=Search&viewParam_context=catalog&viewParam_userid=fef4540077eb04a10caef7ace45dfcaf2248192cf63d&viewParam_keyword=CourseCatalog&viewParam_siteId=icb.site69201&viewParam_siteType=12&viewParam_topicId=icb.topic749225&viewParam_coreToolId=14346&viewParam_urlRoot=coursecatalog.harvard.edu&viewParam_remoteAddr=130.132.173.46&viewParam_permissions=7%2C8&viewParam_pageContentId=icb.pagecontent695860&viewParam_pageid=icb.page335057&viewParam_requestId=8027964#a_icb_pagecontent695860"

numcalls = int(int(9473 / 25) + 1)

with open('harvard.txt', 'w') as f:

	for callMe in range(numcalls):
		formatted = url.format(callMe * 25)
		r = requests.get(formatted)
		soup = BeautifulSoup(r.text)
		
		for tr in soup.find_all('tr'):
			try:
				if tr['class'][0] == 'course':
					cols = tr.find_all('td')
					firstcol = cols[1]
					secondcol = cols[2]
					lst = firstcol.find_all('br')
					pieces = ''.join([i if ord(i) < 128 else ' ' for i in firstcol.text]).strip().split('\n')[0].split('(')
					title = pieces[0]
					time = secondcol.span.text
					course = "("
					for piece in pieces[1:]:
						course += piece

					out = {"title": title,
					"time": time,
					"course": course}
					
					f.write(json.dumps(out) + '\n')
					 
					#print lst[0].text, lst[1].text
			except Exception as e:
				print e
				continue