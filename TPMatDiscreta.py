time1,time2=input().split()
goltime1=int(input())
goltime2=int(input())
parte1arranjo=1
parte2arranjo=1
if goltime1==goltime2:
    print("ainda nao")
elif goltime1>goltime2:
    for i in range(1,goltime1+1):
        parte1arranjo*=i
    for i in range(1,(goltime1-goltime2)+1):
        parte2arranjo*=i
    arranjo=parte1arranjo/parte2arranjo + 1
elif goltime2>goltime1:
    for i in range(1,goltime2+1):
        parte1arranjo*=i
    for i in range(1,(goltime2-goltime1)+1):
        parte2arranjo*=i
    arranjo=parte1arranjo/parte2arranjo + 1
print(arranjo)