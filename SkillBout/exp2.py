def reverse(list):
    return list[::-1]
li=list(map(int,input("Enter any 5 numbers: ").split()))
sums=0
for i in li:
    sums+=i
avg=sums/len(li)
print("reversed list is :",reverse(li))
print("sum :",sums)
print("avg :",avg)