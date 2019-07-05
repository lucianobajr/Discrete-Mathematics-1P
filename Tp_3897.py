#created by luciano
import itertools
casos = []
time1,time2=map(str,input().split(','))
gol1=int(input())
gol2=int(input())
teste = time1+time2
if gol1 == 0 and gol2 == 0:
    print(0)
else:
    casos=sorted(set(''.join(anagrama) for anagrama in itertools.product(teste,repeat=(gol1+gol2))if(anagrama.count(time1)==gol1 and anagrama.count(time2)==gol2)))
    for i in range(len(casos)):
        print(casos[i])
