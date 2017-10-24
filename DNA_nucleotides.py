import sys
a= open(sys.argv[1]).read()

#a = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

print a.count('A'), a.count('C'), a.count('G'), a.count('T')

