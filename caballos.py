import random
hs = []
for i in range (0,25):
     n= random.randint(1,1000)
     hs.append(n)
print("Tiempos de caballos")
print(hs)
print("grupos")

grupos = [[],[],[],[],[]]
k=0
for j in range(0,5):
    for i in range (0,5):
        grupos[j].append(hs[k])
        k=k+1
print(grupos[j])
k=k+5

print("grupos carreras")

for j in range(0,5):
    grupos[j].sort()
    print(grupos[j])
for j in range(1,5):
    gactual=grupos[j]
    actual=grupos[j][4]
    i=j
    while i>0 and grupos[i-1][4]>actual:
        grupos[i]=grupos[i-1]
        i=i-1
    grupos[i]=gactual

print("grupos ordenados por caballo mas rapido en la sexta carrera")

for j in range(0,5):
    print(grupos[j])

print("septima carrera")
lastg=[grupos[3][3],grupos[3][4],grupos[4][2],grupos[4][3],grupos[4][4]]
lastg.sort(reverse=True)
print("primeros")
print(lastg[0],lastg[1])

print("comprobacion")
print("listado 25")
hs.sort(reverse=True)
print(hs)
print("primeros")
print(hs[0],hs[1])