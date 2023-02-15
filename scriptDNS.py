import urllib.request
import os
import re


ip_api = 'curl -X GET https://ipv4.api.hosting.ionos.com/dns/v1/dyndns?q=N2M4YjQ3Mzc1MjQ5NDNlNThkYTM0Zjc3MDEzNzQ0ZDkuYWVwOE4wbzM3UHA3STR4NUE3ejFJWUZoTDV2aExqa05XN3BlaEp1WmJUYkZaTWNyYWhsQUNwamVUcG9wdy1nNzRWWE1ZSWVqS2pjMUFDMXB2dko3SUE'

ip = (urllib.request.urlopen('https://ident.me').read().decode('utf8'))

#ip_log = open("iplog.txt","r").readline(20)

ip_dominio = (urllib.request.urlopen('https://dns.google/resolve?name=calerogr.com&type=A').read().decode('utf8'))
ip_dominio = re.search('data":"(.+?)"}', ip_dominio).group(1)


print("ip dominio:", ip_dominio)
print("ip publica:", ip)
#print("ip de iplog", ip_log)

if ip == ip_dominio:
    print("La ip no ha cambiado")
else:
    print("La ip SI ha cambiado")
    os.system(ip_api)
    #open("iplog.txt","w").write(str(ip))

#ip_log = open("iplog.txt","w")
#ip_log.write(str(ip))
#ip_log.close()