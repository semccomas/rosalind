import sys

f = sys.argv[1]
f = open(f).read().splitlines()
s = f[0]
t = f[1]

c = 0

for ss, tt in zip(s, t):
	if ss != tt:
		c = c + 1


print c