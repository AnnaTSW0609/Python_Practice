"""Using Biopython Module to access Uniprot using accession number"""

from Bio import ExPASy

from Bio import SwissProt

# https://stackoverflow.com/questions/35569042/ssl-certificate-verify-failed-with-python3

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# to circumvent the SSL certificate error 


handle = ExPASy.get_sprot_raw('B5ZC00') #you can give several IDs separated by commas

record = SwissProt.read(handle) # use SwissProt.parse for multiple proteins

for i in record.keywords: # this supposedly contain all info about the Biological Processes
  print(i)
  
