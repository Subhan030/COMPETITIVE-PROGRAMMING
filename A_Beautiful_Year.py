n=int(input())
for i in range(n+1,9013):
    l=list(str(i))
    c1=0
    for j in l:
        c=l.count(j)
        if(c==1):
            c1+=1
        else:
            break
    if(c1==4):
        ans=i
        break
    else:
        continue
print(ans)