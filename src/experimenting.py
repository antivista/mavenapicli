import requests                     # To use request package in current program 
import re
import datetime
import subprocess
import io
import ssl
from cryptography import x509
from cryptography.hazmat.backends import default_backend
#from pyasn1_modules import pem, rfc2459
#from pyasn1.codec.der import decoder

url = 'https://search.maven.org/solrsearch/select'

#artifact_id = '\"com.google.inject\"'
# re.escape('"com.google.inject"')
group_id = 'guice'
artifact_id = 'com.google.inject'
print('artifact_id', artifact_id)
payload = {'q': 'g:' + artifact_id + ' AND a:' + group_id, 'core': 'gav', 'rows': '10', 'wt': 'json'}
print(payload)
#payload = urllib.parse.urlencode(payload)
'''
response = requests.get(url, params=payload) 
#response.encoding = None
#print(response.content)
#print(response.encoding)
#response.encoding = 'ISO-8859-1'
print('URL ->', response.url)


print(response.status_code)     # To print http response code  
#print(response.text)
json_response = response.json() #'\n'.join(response.json())
version = json_response['response']['docs'][0]['v']
timestamp = json_response['response']['docs'][0]['timestamp'] 
date = datetime.datetime.fromtimestamp(timestamp/1000.0).strftime('%Y-%m-%d')
print('version', version)
print('date', date)
'''

#for key, value in json_response.items():
#    print(key, ":", value)

# Get cert
myhostname = 'search.maven.org'
cert = ssl.get_server_certificate((myhostname, 443))
print('cert', cert)
# TODO: save the cert content in a file. NO IS USELESS.

# TODO: decoding info from the cert
cert_decoded = x509.load_pem_x509_certificate(str.encode(cert), default_backend())
print(cert_decoded.serial_number)
print(cert_decoded.signature_algorithm_oid)
print(cert_decoded.signature_hash_algorithm.name)
print(cert_decoded.issuer)
print(cert_decoded.subject)
print(cert_decoded.not_valid_after)
print(cert_decoded.not_valid_before)


'''
Maybe is not legal

try:
    nikto_result = subprocess.Popen(['nikto', '-ssl', '-maxtime', '7', '-h', 'https://search.maven.org/'])
    for line in io.TextIOWrapper(nikto_result.stdout, encoding="utf-8"):  # or another encoding
    # do something with line
        print(line)
except Exception as err:
    print("An error occurred ->", err)
else:
    print(nikto_result)
'''

