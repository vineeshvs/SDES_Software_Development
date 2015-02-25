#!/bin/python
some_var=1
def fib(n):
	"""Print a fib series upto n."""
	a,b=0,1
	while b<n:
		print b,
		a,b=b,a+b

