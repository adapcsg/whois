# Coded By Kaito 
# March 20, 2020

import requests
import json

ascii = """

 __          ___    _  ____ _____  _____ 
 \ \        / / |  | |/ __ \_   _|/ ____|
  \ \  /\  / /| |__| | |  | || | | (___  
   \ \/  \/ / |  __  | |  | || |  \___ \ 
    \  /\  /  | |  | | |__| || |_ ____) |
     \/  \/   |_|  |_|\____/_____|_____/ 
"""

banner = """
  Coded By Kaito | 03/20/2020

"""

def kaito(banner,ascii):
	print ascii
	print banner
	u = raw_input('Target Url-> ')
	r = requests.get('https://api.indoxploit.or.id/domain/'+u)
	x = r.json()
	print " ------[ Ip Address ]-----"
	o = x["data"]["resolutions"]
	for i in o:
		print i["ip_address"]
	print "\n ------[ Sub Domains ]-----"
	f = x["data"]["subdomains"]
	for v in f:
		print v
	print "\n ------[ Geolocation ]-----"
	try:
		b = x["data"]["geolocation"]
		country = b["country"]
		zip = b["zip"]
		proxy = b["proxy"]
		region = b["regionName"]
		mobile = b["mobile"]
		print """country : %s\nZip : %s\nProxy : %s\nRegion : %s\nMobile : %s
		"""%(country,zip,proxy,region,mobile)
	except 'NoneType':
		print "Not supported site"
	
if __name__ == '__main__':
	kaito(banner,ascii)
