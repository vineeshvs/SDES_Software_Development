#!/bin/python
def gcd(a, b):
	while True:
		try:
			print "Validating numbers"
			break
		except ValueError:
			print "Invalid value"
			break
	while b:
		a,b=b,a%b
	return a
