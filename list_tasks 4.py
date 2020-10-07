n=int(input("Enter index of the list "))
a=[]
print("Enter elements to be added in the list: ")
for i in range(0,n):
  b=0
  b=int(input("\n"))
  a.append(b)
print("The original list is: ",a)
temp = 0
for i in range(0,int(n/2)):
  temp = a[i]
  a[i]=a[n-i-1]
  a[n-i-1]=temp
print("The swapped array is ", a)