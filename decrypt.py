czytaj = open("tekst.txt", "r", encoding="utf-8")
#zapisz = open("tekst.txt", "w", encoding="utf-8")

alfabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ ,.?!@1234567890+-*/"
tekst_jawny = czytaj.read().strip()
print(tekst_jawny)
#tekst_jawny = tekst_jawny.upper()
przesuniecie = 5

def szyfr(tekst):
    counter = 1
    for litera in tekst:
        idx_litery = alfabet.index(litera)
        tekst = tekst.replace(alfabet[idx_litery], alfabet[(idx_litery - przesuniecie)], 2)
        print(tekst, counter)
        counter += 1
    return tekst

tekst = szyfr(tekst_jawny)
print(tekst)