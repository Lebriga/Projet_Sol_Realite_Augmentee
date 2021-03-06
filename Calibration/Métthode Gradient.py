import numpy as np

#def gradient(M):

A= np.matrix([[1],[1],[0],[1],[0],[0],[1],[0],[1],[1],[1],[1]])
print(A)
print(int(A[3][0]))


def norme_vecteur(X):
    return((np.transpose(X)*X)[0,0])

def produit_scalaire_vecteurs(X,Y,A="Vide"):
    n = len(X)
    if A=="Vide":
        A=np.matrix(np.eye(n,n))
    p = len(Y)
    m = len(A)
    o = np.size(A)/len(A)
    if n!=p or p!=m or m!=o:
        print ("Produit scalaire avec deux vecteurs de dimensions différentes ou une matice de dimension inadaptée")
        return(0)
    else:
        """Z= np.eye(1,n)
        for i in range (0,n):
            Z[0,i] = X[i,0]
        Z=Z*A
        print(Z)
        print(X)
        S = float(Z*X)
        return(S)"""
        return(((np.transpose(X))*A*Y)[0,0])

def gradient(A,b, x0,eps0, eps1, kmax):
    r = A*x0-b
    #print(A)
    #print(x0)
    #print(b)
    #print(A*x0)
    #print("abcd")
    r0=r
    #print("r: ",r)
    diff_normes_x = eps0+1
    k = 0
    x = x0
    while (diff_normes_x>eps0) and k<=kmax and norme_vecteur(r)>eps1:
        #print(k)
        if k == 0:
            d = r
        else:
            alpha = - (produit_scalaire_vecteurs(r,d,A))/(produit_scalaire_vecteurs(d,d,A))
            d = r + alpha*d
            #print("d", d)
        #print("Produit scalaire:", produit_scalaire_vecteurs(d,d,A))
        rho = - (produit_scalaire_vecteurs(r,d,A))/(produit_scalaire_vecteurs(d,d,A))
        x0, x = x, x + rho*d
        #print(x0 , x)
        r= A*x - b
        k = k + 1
        #print(x-x0)
        diff_normes_x= norme_vecteur(x-x0)
    return(x, k,diff_normes_x)