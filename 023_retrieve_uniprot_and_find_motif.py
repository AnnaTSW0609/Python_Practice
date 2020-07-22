"""REST retrieval of sequences from uniprot using uniprot identifiers"""


# obtain the list of ids from rosalind file 

all_id = "" 

with open("/Users/annatswater/Desktop/uniprot_test.py", "r+") as f:
   
   for line in f:
      
      line = line.replace("\n", "")
      all_id += " "
      all_id += line

all_id = all_id.lstrip()

print(all_id)

# standard database identifier mapping from
# https://www.uniprot.org/help/api_idmapping

# https://stackoverflow.com/questions/35569042/ssl-certificate-verify-failed-with-python3
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


import urllib.parse
import urllib.request

url = 'https://www.uniprot.org/uploadlists/'

params = {
'from': 'ACC+ID',
'to': 'ENSEMBL_ID',
'format': 'tab',
'query': "A2Z669 B5ZC00 P07204_TRBM_HUMAN P20840_SAG1_YEAST"
}

data = urllib.parse.urlencode(params)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as f:
   response = f.read()
print(response.decode('utf-8'))

# N-glycosylation motif is written as N{P}[ST]{P}.
      
