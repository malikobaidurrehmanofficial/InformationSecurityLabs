num=int(input("Enter the number of terms to get fabunaci series : "))



t1=0
t2=1


print(t1,t2,sep="\t",end="\t")

for i in range(3,num+1):
    tn=t1+t2
    t1=t2
    t2=tn
    print(tn,end="\t")
