import sys
try:
    output=open("haromszogszamok.txt","w")
    ls=[]
    sys.argv[1]=int(sys.argv[1])
    for i in range(1,sys.argv[1]):
        a=(i*(i+1))/2
        a=int(a)
        if a<sys.argv[1] and a%2:
            ls.append(a)
            b=str(ls)
    output.write(b)
    print("A háromszög számok haromszogszamok.txben vannak")
except IndexError:
    print("Index!")