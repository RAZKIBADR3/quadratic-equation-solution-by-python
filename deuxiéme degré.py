from math import*
A = float(input("entrer le valeur de A\n"))
B = float(input("entrer le valeur de B\n"))
C = float(input("entrer le valeur de C\n"))
D = B*B-4*A*C
if D>0 :
    X1 = (-B+sqrt(D))/2*A
    X2 = (-B-sqrt(D))/2*A
    print("X1 =" , str(X1))
    print("X2 =" , str(X2))
elif D==0 :
    X = -B/2*A
    print("X =" , str(X))
else :
    print("l'equation n'a pas de solution")
