l=[]
x=[]
q=""
p,r=0,0
t=int(input())
if(t%2==0):
    l=list(map(int,input().split()))
    for i in range(int(t/2)):
        z=str(l[i])
        x.append(z[0])
    for i in range(int(t/2),t):
        z=str(l[i])
        x.append(z[-1])
for i in x:
    q=q+i
w=int(q)
#print(w)
for i in range(len(q)):
    if(i%2!=0):
        p=p+int(q[i])#odd
    else:
        r=r+int(q[i])#even
if(((p-r)%11)==0):
    print("OUI")
else:
    print("NON")
