n=int(input())
m=list(map(int,input().split()))
l=m[:]
maxi=max(l)
mini=min(l)
c=0
for i in range(n):
    if(l[i]==mini):
        min_index=i
    
max_index=l.index(maxi)
if(max_index>min_index):
    print(max_index-1+n-min_index-1)
else:
    print(max_index-1+n-min_index)
