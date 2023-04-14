def greetin(name,message="hello"):
    print(message+ " "+name)


greetin("rama")
greetin("meikan","mambo")

def maxvalue(a,b,c,d,e,f,g):
    return  max(a,b,c,d,e,f,g)
myanswer=maxvalue(34,1,4,5,6,23,56)
print(myanswer)

def minvalue(a,b,c,d,e,f,g,h):
    return min(a,b,c,d,e,f,g,h)
myresults=minvalue(12,34,23,4,554,56,6,1)
print(myresults)

def sortvalue(i,j,k,l,m):
    return sorted(i,j,k,l,m)
mydata=sortvalue(2030,4032,4561,3421,7546)
print(mydata)