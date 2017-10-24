import sys
import numpy as np
f = open(sys.argv[1]).read()

f = f.replace('\n', '')
f = f.split('>')

gc = []
names = []
for line in f[1:]:
	name = line[0:13]
	seq = line[13:]
	gc.append((seq.count('G') + seq.count('C'))/ float(len(seq)) * 100)
	names.append(name)

gc = np.asarray(gc)
names = np.asarray(names)
w = np.where(gc == max(gc))
print names[w]
print max(gc)