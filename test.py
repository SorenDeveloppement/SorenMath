from fraction import Fraction


def calcul(n, n_iter, result):
    if n == n_iter:
        result += 1
        return Fraction(2)

    return result + (1 + Fraction(1, calcul(n + 1, n_iter, result)))


c1 = calcul(0, 19, 0).irreducible()
c2 = calcul(0, 50, 0).irreducible()

print(
    '*' * 80 + '\n',
    '\n',
    ' ' * 10 + "Calcul 1: " + str(c1.irreducible()) + "  =  " + str(c1.decimal()) + '\n',
    '\n',
    '*' * 80 + '\n',
    '\n',
    ' ' * 10 + "Calcul 2: " + str(c2.irreducible()) + "  =  " + str(c2.decimal()) + '\n',
    '\n',
    '*' * 80
)

"""

Output:

********************************************************************************
 
           Calcul 1: 17711/10946  =  1.618033985017358
 
 ********************************************************************************
 
           Calcul 2: 53316291173/32951280099  =  1.618033988749895
 
 ********************************************************************************

"""
