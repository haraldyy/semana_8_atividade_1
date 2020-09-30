def lista():
    lista=[]
    soma=0
    produto=1
    for w in range(10):
        n=int(input())
        soma+=n
        produto*=n
        lista.append(n)
    print(lista)
    print(soma)
    print(produto)
def main():
    lista()
if __name__=='__main__':
    main()

    
