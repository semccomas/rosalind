import sys
f = open(sys.argv[1]).read().splitlines()
import numpy as np
l = len(f[1])
l = np.zeros((4,l))


for line in f:
	if '>' not in line:
		for char in line:
