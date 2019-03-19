import math
print("Enter the number to factor of form (p*q):	")
n=int(input())
t0=math.ceil((math.sqrt(n)))
counter=0
ans=math.sqrt(pow((t0+counter),2)-n)
while(not float(ans).is_integer()):
	counter+=1
	ans=math.sqrt(pow((t0+counter),2)-n)
t=t0+counter
s=ans
p=t-s
q=t+s
print("Your first number	",int(p))
print("Second	number	",int(q))

