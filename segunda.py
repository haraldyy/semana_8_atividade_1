def listas():
    t=int(input())
    lista=[]
    for w in range(t):
        lista.append(0)
    print(lista)
    lista=[]
    numero=1
    while numero<=t:
        lista.append(numero)
        numero+=1
    print(lista)
    lista=[]
    for w in range(t):
        n=int(input())
        lista.append(n)
    print(lista)
    lista=[]
    for w in range(t):
        n=int(input())
        lista.insert(0,n)
    print(lista)
def main():
    listas()
if __name__=='__main__':
    main()
