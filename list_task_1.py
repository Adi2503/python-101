#The code is used to find the largest and the second largest item in a list


n = int(input("Enter the size of the list"))
a=[]
for i in range(0,n):
    b=0
    b=int(input("Enter the element "))
    a.append(b)
a.sort()
print("The largest element is: ", a[-1])
print("The second largest element is: ",a[-2])
