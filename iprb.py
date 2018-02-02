k = 24
m = 16
n = 27

# 3 probabilities, 1/4 d, 1/2 d/r, 1/4 r prob of one event happening is sum of all outcomes. 

'''
P dom = 1(k + m), 1(k + k), 1(k + n), 3/4(m + m) / total
P not = 1(n + n), 1/2(m + n), 1/4(k+n) / total

5 mating probabilities

Pk = 2/6 k1 k2 k3 k4 k5 k6    2=1 3=3 4=6 5=10 6=16  
Pm = 2/6 m1 m2
Pn = 2/6 n1 n2

Pk+k = 1/15 * 1 = 1/15 = 0.067
Pk+m = 4/15 * 1 = 4/15 = 0.267
Pk+n = 4/15 * 1 = 4/15 = 0.267
Pm+m = 1/15 * 3/4 = 0.05
Pm+n = 4/15 * 1/2 = 0.1333
Pn+n = 1/15 * 0 = 0 


P dom = sum of all ^^^ == 0.7833
'''

def sum_self(s):
	v = 0
	for val in xrange(s):
		s = s - 1
		v = v + s
	return v

#sum_self = what you see above with pk, need to know how many times k could mate with other k 

Pkk = sum_self(k)
Pkm = (k * m)
Pkn = (k * n)
Pmm = sum_self(m)
Pmn = (m * n)
Pnn = sum_self(n)

tot = Pkk + Pkm + Pkn + Pmm + Pmn + Pnn
tot = float(tot)
Pkk = (Pkk/tot) * 1 
Pkm = (Pkm/tot) * 1
Pkn = (Pkn/tot) * 1
Pmm = (Pmm/tot) * 0.75
Pmn = (Pmn/tot) * 0.5
Pnn = 0

tot = Pkk + Pkm + Pkn + Pmm + Pmn + Pnn


print tot