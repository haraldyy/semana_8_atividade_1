def listas():
    numbers=[]
    par=[]
    impar=[]
    for i in range(20):
        n=int(input())
        numbers.append(n)
        if n%2==0:par.append(n)
        else:impar.append(n)
    print(numbers)
    print(par)
    print(impar)
def main():
    listas()
if __name__=='__main__':
    main()
