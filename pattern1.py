def pyr(a):
    for i in range(1,a+1):
        for j in range(1,i+1):
            print(i*j,end="\t")
        print("\n")
a=int(input("Enter Limit"))
pyr(a)
