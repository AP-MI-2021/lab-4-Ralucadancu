def init_lst():
    return []

def is_superprime(n):
    while n!=0:
        if n<2 : return False
        for i in range(2,n):
            if n%i==0: return False
        n=n // 10
    return True

def numere_superprime(lst):
    for nr in lst:
        if is_superprime(nr):
            print(nr)

def ultima_cifra(nr,c):
    if nr %10==c:
        return True
    else : return False


def numere_ultima_cifra (lst,c):
    mini=-99999999
    for nr in lst:
        if ultima_cifra(nr,c):
            if nr<mini: mini=nr

    return mini

def numere_negative(lst):
    for nr in lst:
        if nr<0:
            print(nr)


def citire_lista():
    lst=input("Lista de numere este :(cu virgula intre ele)")
    lst=lst.split(",")
    lst=[int(el) for el in lst]
    return lst


def print_meniu():
    print("1.Cititi o lista cu numere intregi ")
    print("2.Afisati numerele negative nenule din lista")
    print("3.Afisati cel mai mic numar care are ultima cifra egala cu o cifra citita")
    print("4.Afisati toate numerele din lista care sunt superprime")
    print("5.Afisati lista obtinuta in urma apelarii functiei")
    print("6.Iesiti din aplicatie")


def run_meniu():
    lst=init_lst()

    while True:
        print_meniu()
        try:
            n=int (input("Selectati ce doriti sa facem in contiuare: "))
            if n<0 or n>5:
                raise ValueError
            elif n==1 :
                lst=citire_lista()
            elif n==2 :
                print("Numerele negative din lista sunt:")
                numere_negative(lst)
            elif n==3 :
                c=int(input("Introduceti cifra :"))
                rez=ultima_cifra(lst,c)
                print("Cel mai mic numar care are ultima cifra  egala cu  cifra citita: " + str(rez))
            elif n==4:
                print("Numerele superprime din lista sunt:")
                numere_superprime(lst)
            elif n==6 :
                return
        except ValueError:
            print("Va rog introduceti un numar valid.\n")

run_meniu()






