"""
In Legendre Symbol we introduced a fast way to determine whether a number is a square root modulo a prime. We can go further: there are algorithms for efficiently calculating such roots. The best one in practice is called Tonelli-Shanks, which gets its funny name from the fact that it was first described by an Italian in the 19th century and rediscovered independently by Daniel Shanks in the 1970s.

All primes that aren't 2 are of the form p ≡ 1 mod 4 or p ≡ 3 mod 4, since all odd numbers obey these congruences. As the previous challenge hinted, in the p ≡ 3 mod 4 case, a really simple formula for computing square roots can be derived directly from Fermat's little theorem. That leaves us still with the p ≡ 1 mod 4 case, so a more general algorithm is required.

In a congruence of the form r2 ≡ a mod p, Tonelli-Shanks calculates r.

Tonelli-Shanks doesn't work for composite (non-prime) moduli. Finding square roots modulo composites is computationally equivalent to integer factorization.


The main use-case for this algorithm is finding elliptic curve co-ordinates. Its operation is somewhat complex so we're not going to discuss the details, however, implementations are easy to find and Sage has one built-in.

Find the square root of a modulo the 2048-bit prime p. Give the smaller of the two roots as your answer.
"""

from winreg import QueryValueEx
from crypty import *

def getInput(filePath):
    
    fp = open(filePath)

    for i, line in enumerate(fp):
        if i == 0:
            a = int(line.split(" ")[2])
        elif i == 1:
            p = int(line.split(" ")[2])

    fp.close()

    return a, p


def main():
    filePath = "modularArithmetic\ModularSquareRoot-output.txt"

    a, p = getInput(filePath)

    x = getModularSquareRoot(a, p)
    print(x)
    print()
    print(-x%p)

if __name__ == "__main__":
    main()


###
### Flag: 2362339307683048638327773298580489298932137505520500388338271052053734747862351779647314176817953359071871560041125289919247146074907151612762640868199621186559522068338032600991311882224016021222672243139362180461232646732465848840425458257930887856583379600967761738596782877851318489355679822813155123045705285112099448146426755110160002515592418850432103641815811071548456284263507805589445073657565381850521367969675699760755310784623577076440037747681760302434924932113640061738777601194622244192758024180853916244427254065441962557282572849162772740798989647948645207349737457445440405057156897508368531939120
###