#!/usr/bin/python3

import urllib.request
import requests
from bs4 import BeautifulSoup

domain = input("Input domain to buffer without http or https: ")
print(domain)

buffer = domain

r = requests.get("https://dns.bufferover.run/dns?q={buffer}".format(buffer=buffer))
if r.status_code == 200:
    print('Successful request!')
    content = r.content
    #print(content)
    soup = BeautifulSoup(content, 'html.parser')
    print(soup)
