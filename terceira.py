def listas():
    t=int(input())
    lista=[]
    for w in range(t):
        n=float(input())
        lista.insert(0,n)
    print(lista)
    lista=[]
    nota=0
    for w in range(t):
        nota=float(input())
        lista.append(nota)
    print(lista)
    if nota==0  or t==0:
        print('SEM NOTAS')
    if nota!=0:
        media=sum(lista)/len(lista)
        print(f'{media:.1f}')
    
    vogais=[]
    consoantes=[]
    for w in range(t):
        letra=str(input())[0]
        if letra.lower() in 'aeiou':
            vogais.append(letra)
        else:
            consoantes.append(letra)
    print(len(vogais))
    print(consoantes)
def main():
    listas()
if __name__=='__main__':
    main()
