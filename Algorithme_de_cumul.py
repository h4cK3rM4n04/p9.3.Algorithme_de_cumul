def moyenne(T) :
    res = 0
    for x in T:
        res += x
        c = res / len(T)
    return c

assert moyenne([1,2,3]) == 2.0
assert moyenne([10,20,13,14,8,11]) == 12.666666666666666
assert moyenne([10]) == 10.0

def moyenne(T) :
    res = 0
    for x in T:
        res += x
        c = res / len(T)
    return c

def compte_moyenne(T):
    x = moyenne(T)
    y = len(T)
    return x, y

assert compte_moyenne([10]) == (10.0, 1)
assert compte_moyenne([i for i in range(100)]) == (49.5, 100)
assert compte_moyenne([i**2 for i in range(50)]) == (808.5, 50)

def somme_sum(T):
    v = 0
    for x in T:
        v += x
    return v

def var_moy(T):
    v = moyenne(T)
    sum_c = somme_sum([x ** 2 for x in T])
    mcv = sum_c / len(T)
    ms = moyenne(T) ** 2
    res = mcv - ms
    return v, res

assert var_moy([1,1,1]) == (1.0, 0.0)
assert var_moy([1,0,2]) == (1.0, 0.6666666666666667)
assert var_moy([0,0,3]) == (1.0, 2.0)
assert var_moy([i for i in range(50)]) == (24.5, 208.25)

def pairs(T):
    cpt = 0
    for x in T:
        if x == 0:
            continue
        elif x % 2 == 0:
            cpt += 1
    return cpt

assert pairs([1,1,1]) == 0
assert pairs([2]) == 1
assert pairs([2,1,2,1,2]) == 3
assert pairs([2,1,0,1,2]) == 2