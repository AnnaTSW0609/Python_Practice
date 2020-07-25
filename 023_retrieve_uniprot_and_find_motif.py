"""Retrieve protein sequences uniprot accession numbers using Biopython modules"""
"""Then use Regex module to scan for pattern, e.g. N-glycosylation motif"""
"""Then return the position of the motif"""


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

# [XY] means "either X or Y" and {X} means "any amino acid except X." 
# For example, the N-glycosylation motif is written as N{P}[ST]{P}.
# so it's N-(not P)-(either S or T)-(not P)

import re # import the re module for parsing 
motif = r"N[^P](S|T)[^P]" # https://pythonforbiologists.com/regular-expressions

for item in ID_and_seq:
   pos = [] # collection of all positions
   pos.append(re.search(motif, ID_and_seq[item]).start())
   
