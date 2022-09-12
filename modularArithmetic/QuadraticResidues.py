"""
We can say that an integer 'x' is a Quadratic Residue if there exists and 'a' such that:

a^2 = x mod p

If there is no such solution, then the integer is a Quadratic Non-Residue.

Every Quadratic Residue has exactly two 'roots' which are 'a' and '-a'.

"""

p = 29
ints = [14, 6, 11]

residues = []

for num in ints:
	for i in range(p):
		if pow(i, 2, p) == num:
			residues.append((num, [i, -i%p]))
			break

for tup in residues:
	print(f"Residue: {tup[0]}\tRoots: {tup[1]}")

###
###	Flag: 8
###