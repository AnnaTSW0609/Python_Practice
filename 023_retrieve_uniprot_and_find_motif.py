"""Retrieve protein sequences uniprot accession numbers using Biopython modules"""
"""Then use Regex module to scan for pattern, e.g. N-glycosylation motif"""
"""Then return the position of the motif"""


# obtain the list of ids from rosalind file 

all_id = [] 

with open("/Users/annatswater/Desktop/rosalind_mprt.txt", "r+") as f:
   
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
import regex # https://stackoverflow.com/questions/34774126/re-finditer-returning-same-value-for-start-and-end-methods
motif = r"N[^P](S|T)[^P]" # https://pythonforbiologists.com/regular-expressions

position = {} # a dictionary to store the accession number and the list of matches (indices)
index = 0 # initialize starting position, so that wouldn't miss those closely together 

# Method from https://www.cnblogs.com/think-and-do/p/7283840.html
# Regex version of method from https://www.geeksforgeeks.org/python-count-overlapping-substring-in-a-given-string/


# This one from 
# https://stackoverflow.com/questions/2674391/python-locating-the-position-of-a-regex-match-in-a-string
# to return multiple matches and their positions
# but will miss overlaps

# Sol 1: use regex, which has overlapped parameter in finditer

# Sol 2: http://rosalind.info/problems/mprt/solutions/
# Hascool actually does have it right,
# because he uses '(?=N[^P][ST][^P])',
# which matches all '' (no character) that is followed by the motif,
# without actually consuming the motif. Overlapping matches will be found.

for item in ID_and_seq:
   # these two lines search for multiple matches 
   iter = regex.finditer(motif, ID_and_seq[item], overlapped=1)
   indices = [m.start()+1 for m in iter]
   # this line saves the list of matches to the dict
   position [item] = indices

# to return the answer in Rosalind format
for entry in position:
   if position[entry] != []:
      print(entry)
      print(*position[entry])
