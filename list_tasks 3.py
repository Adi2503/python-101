n = int(input("Enter size of first list"))
m = int(input("Enter size of second list"))
print("Enter elements of first array")
a = []
b = []
for i in range(0,n):
    c=0
    c=int(input("\n"))
    a.append(c)
for i in range(0,m):
    d = 0
    d = int(input("\n"))
    b.append(d)
e=[]
e=a+b
e.sort()
print("Sorted list is ", e)
