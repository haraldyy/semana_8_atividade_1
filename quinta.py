def listas():
    a=[]
    b=[]
    c=[]
    for w in range(25):
        n=int(input())
        a.append(n)
    for w in range(25):
        n=int(input())
        b.append(n)
    for w in range(25):
        n=a[w]
        c.append(n)
        n=b[w]
        c.append(n)
    print(a)
    print(b)
    print(c)
def main():
    listas()
if __name__=='__main__':
    main()
    
    
