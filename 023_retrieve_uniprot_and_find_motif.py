"""REST retrieval of sequences from uniprot using uniprot identifiers"""


# obtain the list of ids from rosalind file 

all_id = [] 

with open("/Users/annatswater/Desktop/uniprot_test.py", "r+") as f:
   
   for line in f:
      
      line = line.replace("\n", "")
      
      all_id.append(line)


# to circumvent the SSL certificate error
# https://stackoverflow.com/questions/35569042/ssl-certificate-verify-failed-with-python3
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


"""Using Biopython Module to access Uniprot using accession number""" # borrowed from exercise 26

from Bio import ExPASy

from Bio import SwissProt

# Reference: https://biopython.readthedocs.io/en/latest/chapter_uniprot.html#sec-expasy-swissprot

records = []


for accession in all_id: # obtain the raw uniprot data

    handle = ExPASy.get_sprot_raw(accession)
    record = SwissProt.read(handle)
    records.append(record)

ID_and_seq = {} # create a dictionary for storing the sequences under their accession number

for item, accession in zip(records,all_id):
    
    ID_and_seq [accession] = item.sequence # reference: http://rosalind.info/problems/dbpr/


