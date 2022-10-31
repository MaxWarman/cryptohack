"""
The Chinese Remainder Theorem gives a unique solution to a set of linear congruences if their moduli are coprime.

This means, that given a set of arbitrary integers ai, and pairwise coprime integers ni, such that the following linear congruences hold:

Note "pairwise coprime integers" means that if we have a set of integers {n1, n2, ..., ni}, all pairs of integers selected from the set are coprime: gcd(ni, nj) = 1.

There is a unique solution x ≡ a mod N where N = n1 * n2 * ... * nn.

In cryptography, we commonly use the Chinese Remainder Theorem to help us reduce a problem of very large integers into a set of several, easier problems.

Given the following set of linear congruences:

x ≡ 2 mod 5
x ≡ 3 mod 11
x ≡ 5 mod 17

Find the integer a such that x ≡ a mod 935

Starting with the congruence with the largest modulus, use that for x ≡ a mod p we can write x = a + k*p for arbitrary integer k.
"""

"""
x = 2 + 5*a
x = 3 + 11*b
x = 5 + 17*c
"""

import crypty

def checkModuli(n_list):
    if len(n_list) <= 1:
        errorMessage = f"At least two moduli required, {len(n_list)} moduli given..."
        raise ValueError(errorMessage)
    for i in range(len(n_list)-1):
        for j in range(1, len(n_list)):
            if i == j:
                continue

            tmp_gcd = crypty.getGCD(n_list[i], n_list[j])
            if crypty.getGCD(n_list[i], n_list[j]) != 1:
                errorMessage = f"Moduli {n_list[i]} and {n_list[j]} are not coprime - GCD = {tmp_gcd}"
                raise ValueError(errorMessage)


# Solve system of two congruence equations
#   x = a1 (mod n1)
#   x = a2 (mod n2)
def solvePairCRT(a1, n1, a2, n2):
    N = n1 * n2

    m1, m2 = crypty.getGcdCoefficients(n1, n2)

    x = (a1 * n2 * m2 + a2 * n1 * m1) % N
    return x

# Find A in system of congruence equations:
#   x = a1 (mod n1)
#   x = a2 (mod n2)
#   ...
#   x = a_k (mod n_k)
#
# Solution: x = A (mod N = n1*n2*...*n_k)
def solveChineseRemainderTheorem(a_list, n_list): 
    checkModuli(n_list)

    A = a_list[0]
    N = n_list[0]
    for i in range(1, len(n_list)):
        A = solveCRT(A, N, a_list[i], n_list[i])
        N *= n_list[i]

    return A, N

def main():
    a_list = [2,3,5]
    n_list = [5,11,17]
    A, N = solveChineseRemainderTheorem(a_list, n_list)

    print(f"x = {A} (mod {N})")
    

if __name__ == "__main__":
    main()

#
# Answer: x = 872 (mod 935)
#