<<<<<<< HEAD
<<<<<<< HEAD
n = int(input())

s = input().split()

k = 0

for i in range(n):
    if (int(s[i-1])>=0 and int(s[i])>=0) or (int(s[i-1])<0 and int(s[i])<0):
        k+=1

if k == 0:
    print("NO")
else:
=======
n = int(input())

s = input().split()

k = 0

for i in range(n):
    if (int(s[i-1])>=0 and int(s[i])>=0) or (int(s[i-1])<0 and int(s[i])<0):
        k+=1

if k == 0:
    print("NO")
else:
>>>>>>> f48f5ba894d0a2b98ecdf54c818f30cfd9250472
=======
n = int(input())

s = input().split()

k = 0

for i in range(n):
    if (int(s[i-1])>=0 and int(s[i])>=0) or (int(s[i-1])<0 and int(s[i])<0):
        k+=1

if k == 0:
    print("NO")
else:
>>>>>>> 00a100397296f3496da058618e66ccd8e3095b40
    print("YES")