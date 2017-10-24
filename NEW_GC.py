import sys
from Bio import SeqIO
from Bio.SeqUtils import GC

l = [ ] 
for rec in SeqIO.parse(sys.argv[1], 'fasta'):
	tup = (GC(rec.seq), rec.name)
	l.append(tup)

a= max(l)
print a[1], '\n', a[0]