generator = (x*x*x for x in range(5))
for k in generator:
    print(k)

for k in generator:
	print(k)
#Ekrana hiçbir şey basılmaz, çünkü generator'u bir kere kullandık ve bitti
print("*"*45)

def creategeneratorSquare(l):
	for x in l:
	    yield x * x
	
generator = creategeneratorSquare([1,2,3,4,5])
for k in generator:
	print (k) 