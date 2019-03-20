## A Little Theory on Fermat Factorizaion
Fermat factorization can be used to factor a number which is a multiple of 2 close "prime number" i.e. n=p*q form.

The number gets factored down very efficiently within seconds if it is of the above form.

## ALGORITHM
Put t₀=ceil(sqrt(n))

then find sqrt(pow((t₀+1),2)-n),sqrt(pow((t₀+2),2)-n),sqrt(pow((t₀+3),2)-n),........

until the value of the sqrt will be a natural number.

Let's Take an example for n : 678081097161691654731614143911409179

Step 1  : put t₀=ceil(sqrt(n))  ->  t₀=823456797386293761

Step 2  : sqrt(pow((t₀+1),2)-n) ->  1527353709.7374346  not a natural number :(

Step 3  : sqrt(pow((t₀+2),2)-n) ->  1994924296.6642346  not a natural number :(

Step 4  : sqrt(pow((t₀+3),2)-n) ->  2372053233.8448644  not a natural number :(

.

.


when t₀+41 the result of sqrt(pow((t₀+41),2)-n) comes out to be a natural number which is 8258895395

So our s=8258895395

t = t₀+41 = 823456797386293802

So one number will be (p) : t+s = 823456805645189197

Other number (q)  : t-s = 823456789127398407

```markdown
Function for fermat factor 

# Code 
def fermat(n):
	t0=isqrt(n)+1
	counter=0
	t=t0+counter
	temp=isqrt((t*t)-n)
	while((temp*temp)!=((t*t)-n)):
		counter+=1
		t=t0+counter
		temp=isqrt((t*t)-n)
	s=temp
	p=t+s
	q=t-s
	return p,q
 
```
