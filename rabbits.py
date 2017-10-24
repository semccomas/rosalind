#first number is n = number months. second # is k pairs produced
#any month will have rabbits from past, plus new offspring. # offspring Fn = Fn-2 
# => Fn = Fn-1 + Fn-2 

n = 35
k = 5 

#start with 1 pair. Return number of PAIRS that are present after one generation
#F1 = 1
#F2 = 1
#F3 = F2 + k(F1)
#F4 = F3 + k(F2)
F = []
for i in xrange(n):
	if i == 0 or i == 1:
		F.append(1) 
	else:
		F.append(F[i-1] + k*F[i-2])
		
print F
print F[-1] 
