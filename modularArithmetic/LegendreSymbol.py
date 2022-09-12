"""
Now for the flag. Given the following 1024 bit prime and 10 integers, find the quadratic residue and then calculate its square root; the square root is your flag. Of the two possible roots, submit the larger one as your answer.

So Legendre's symbol tells us which integer is a quadratic residue, but how do we find the square root?!
The prime supplied obeys p = 3 mod 4, which allows us easily compute the square root. The answer is online, but you can figure it out yourself if you think about Fermat's little theorem.

Solution:

Aparently there exists a property that for:
	- b - Quadriatic Residue
	- p = 3 (mod 4)
defines roots of 'b' as: +- b^((p+1)/4). Thus we are able to easily find both roots of found QR.

"""
from crypty import *

def getInput(filePath):
	ints = []
	firstLine = True
	for line in open(filePath, "rt"):
		if firstLine:
			p = int(line)
			firstLine = False
		else:
			ints.append(int(line))

	return p, ints

def getQuadraticResudues(ints, p):
	quadraticResidues = []

	for number in ints:
		if getLegendreSymbol(number, p) == 1:
			quadraticResidues.append(number)

	return quadraticResidues

if __name__ == "__main__":

	filePath = "G:\Programowanie\Crypto-Division\cryptohack\modularArithmetic\LegendreSymbol-output.txt"
	p, ints = getInput(filePath)

	quadraticResidues = getQuadraticResudues(ints, p)

	root = pow(quadraticResidues[0],(p+1)//4,p)

	roots = [root]
	if -root%p > root:
		roots.append(-root%p)
	else:
		roots.insert(0, -root%p)

	for ind, r in enumerate(roots):
		print(f"Root #{ind+1}: {r}")


###
###	Flag: 93291799125366706806545638475797430512104976066103610269938025709952247020061090804870186195285998727680200979853848718589126765742550855954805290253592144209552123062161458584575060939481368210688629862036958857604707468372384278049741369153506182660264876115428251983455344219194133033177700490981696141526
###