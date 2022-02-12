import collections;

N = int(input())
D = collections.OrderedDict()

for i in range(N):
    WORD = input()
    if WORD in D:
        D[WORD] +=1
    else
        D[WORD] =1

print(len(D));

for K,V in D.items():
    print(V,end = " ");
