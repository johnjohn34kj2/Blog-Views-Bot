import requests
import time
import sys
from torrequest import TorRequest

headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
}

#Default Tor port configuration
proxyPort=9050
ctrlPort=9051
site = raw_input("Enter your Blog Address : ")
blog = input("Enter The number of Viewers : ")


def run():
     response = tr.get(site, headers=headers,verify=False)
#     time.sleep(10)
     print(response.text)  
     tr.reset_identity()
  


if __name__ == '__main__':
	if len(sys.argv) > 3:
	   if sys.argv[1] and sys.argv[2]:
		proxyPort=sys.argv[1]
		ctrlPort=sys.argv[2]	
	with TorRequest(proxy_port=proxyPort, ctrl_port=ctrlPort, password=None) as tr:
	    for i in range(blog):
		  run()
		
			


			
