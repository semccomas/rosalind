import sys
f= open(sys.argv[1]).read()

a= f[::-1]

l = ""
for line in a:
	if line == 'G':
		l+='C'
	if line =='C':
		l+='G'
	if line == 'T':
		l+='A'
	if line == 'A':
		l+='T'

print l