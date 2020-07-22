"""Biopython 1: counting 4 types of nucleotide in sequence"""

import time

start = time.time()

from Bio.Seq import Seq # using biopython package

sequence = Seq(input("your sequence: "))

lst_ans = []

for x in ["A", "C", "G", "T"]:

    lst_ans.append(sequence.count(x))


print(*lst_ans)

end = time.time()
print(end - start)
