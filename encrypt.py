
try:
    czytaj = open("tekst.txt", "r", encoding="utf-8")

except:
    zapisz = open("tekst.txt", "w", encoding="utf-8")

zapisz = open("tekst.txt", "w", encoding="utf-8")

alfabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ ,.?!@1234567890+-*/"
tekst_jawny = input("Podaj tekst do zaszfrowania: ")
tekst_jawny = tekst_jawny.upper()
przesuniecie = 5

def szyfr(tekst):
    for litera in tekst:
        idx_litery = alfabet.index(litera)
        tekst = tekst.replace(alfabet[idx_litery], alfabet[(idx_litery + przesuniecie) % len(alfabet)])
    return tekst

tekst = szyfr(tekst_jawny)
zapisz.write(tekst)



