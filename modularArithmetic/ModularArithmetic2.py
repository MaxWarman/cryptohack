"""
The integers modulo p (prime) define FIELD denoted as F_p

If the modulus is not prime, the set of integers modulo n define a RING 

Fermat's Little Theorem <- Małe twierdzenie Fermata

	- a^p mod p = a mod p

						1, if a mod p != 0
	- a^(p-1) mod p = 
						0, if a mod p == 0


"""

### Example



showExample = True

if showExample:
	p = 17
	maxRange = 20
	
	# a mod p
	for a in range(1, maxRange):
		mod = a**p % p
		print(f"{a}: {mod}", end=",\t")
	print("")

	# 0 if a mod p = 0 or 1 if not
	for a in range(1, maxRange):
		mod = a**(p-1) % p
		print(f"{a}: {mod}", end=",\t")
	print("")

	# Zeros only
	for exp in range(1, p):
		a = p
		mod = a**exp % p
		print(f"{exp}: {mod}", end=",\t")
	print("")

### Exercise

# 273246787654 ^ 65536 mod 65537 = ?

# Using Fermat's Little Theorem we can tell that 273246787654 ^ 65536 mod 65537 is either 0 or 1 depending on the fact whether 273246787654 mod 65537 == 0 or not respectively

a = 273246787654
p = 65537

print("0") if a % p == 0 else print("1")

###
###	Flag: 1
###