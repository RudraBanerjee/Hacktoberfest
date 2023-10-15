def gcd(l1,l2,c=0):
    l1 = list_create(l1,a)
    l2 = list_create(l2,b)
    n=len(l1)
    n1=len(l2)
    for i in range(n - 1, -1, -1):
        for j in range(n1 - 1, -1, -1):
            if (l1[i] == l2[j]):
                return(print("The GCD is: ", l1[i]))
                c = 1
                break
        if (c == 1):
            break
def list_create(l,a):
    for i in range(1, a + 1):
        if (a % i == 0):
            l.append(i)
    return (l)
a = int(input("Enter the first no.: "))
b = int(input("Enter the second no.: "))
l1=[]
l2=[]
x= gcd(l1,l2)
