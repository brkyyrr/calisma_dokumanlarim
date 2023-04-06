kume={}
kume= {"Python",'c',4,"Cahit"}


########## Metotlar

kume ={1,2,3,4,5}
kume.add(6)
print(kume)

print("\n"+"-"*45 +"\n")

kume ={1,2,3,4,9,6}
kume_yedek =set()
kume_yedek=kume.copy()
print(kume_yedek)

print("\n"+"-"*45 +"\n")

kume ={1,2,3,4,5,6}
kume_2={7,8,9,10}
kume.update(kume_2)
print(kume)

print("\n"+"-"*45 +"\n")

kume ={1,2,3,4,5,6}
kume.remove(4)
print(kume)

print("\n"+"-"*45 +"\n")

kume ={1,2,3,4,5,6}
kume.discard(8)
print(kume)  

print("\n"+"-"*45 +"\n")

kume ={1,2,3,4,5,6}
kume.pop()
print(kume)   

print("\n"+"-"*45 +"\n")

A = {1,2,3,4,9}
B = {3,4,5,6,10}
C = {4,7,8,9,10}
print(A.union(B))   

print("\n"+"-"*45 +"\n")

print(A.intersection(C))

print("\n"+"-"*45 +"\n")

A = {1,2,3,4,9}
B = {3,4,5,6,10}
C = {4,7,8,9,10}
A.intersection_update(C)
print(A)   

print("\n"+"-"*45 +"\n")

A = {1,2,3,4,9}
B = {3,4,5,6,10}
C = {4,7,8,9,10}
print(A.difference(B))   

print("\n"+"-"*45 +"\n")

A = {1,2,3,4,9}
B = {3,4,5,6,10}
C = {4,7,8,9,10}
A.difference_update(B)
print(A) #  

print("\n"+"-"*45 +"\n")

A = {1,2,5,8,9,12}
B = {1,2,5}
print(B.issubset(A))   

print("\n"+"-"*45 +"\n")

print(A.issuperset(B))   

print("\n"+"-"*45 +"\n")

kisitli_kume = frozenset(["Python",3.14,5,'A'])
print(kisitli_kume)

frozenset({5, 3.14, 'Python', 'A'})
kisitli_kume.remove("Python")
