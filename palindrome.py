
for i in range(100,2000):
    s=0 
    a=i
    while(a>0):
     p = a%10
     a = a//10
     s = s*10+p
    if(i==s):
       print(i)