"""
Find multiplicative inverse d: 3 * d = 1 mod 13

				1, if a mod p != 0
a^(p-1) mod p = 
				0, if a mod p == 0

Using this form of Fermat's Little Theorem, if a % p != 0, we can say that:

a^(p-1) mod p = a * a^(p-2) mod p = 1

Thus, the multiplicative inverse of a is a^(p-2) mod p.

"""

p = 13
a = 3

if a % p != 0:
	inverse = a**(p-2) % p
	print(inverse)

###
###	Flag: 9
###