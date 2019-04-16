<<<<<<< HEAD
<<<<<<< HEAD
import math
a = int(input())
count = 0

for i in range(1,int(math.sqrt(a))):
	if a%i==0:
            count+=1
if a%int(math.sqrt(a))==0:
	print(2*count+1)
else:
=======
import math
a = int(input())
count = 0

for i in range(1,int(math.sqrt(a))):
	if a%i==0:
            count+=1
if a%int(math.sqrt(a))==0:
	print(2*count+1)
else:
>>>>>>> f48f5ba894d0a2b98ecdf54c818f30cfd9250472
=======
import math
a = int(input())
count = 0

for i in range(1,int(math.sqrt(a))):
	if a%i==0:
            count+=1
if a%int(math.sqrt(a))==0:
	print(2*count+1)
else:
>>>>>>> 00a100397296f3496da058618e66ccd8e3095b40
	print(2*count)