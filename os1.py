l=[]
s=int(input("Enter the no of softwares: "))
for ele in range(s):
    ele=input("enter softwares:")
    l.append(ele)
l1=[] #burst time values
for ele in range(s):
    ele=int(input("enter values"))
    l1.append(ele)
l2=[] #completion time
count=0
for i in range(s):
    count=count+l1[i]
    l2.append(count)
l3=[]   #arrival time
for i in range(s):
    ele=int(input("enter arrival time values"))
    l3.append(ele)
l4=[]  #turn arround time
for i in range(s):
    tat=l4.append(l2[i]-l3[i])
l5=[]  #wait in time
for i in range(s):
    wit=l5.append(l4[i]-l1[i])
m=0
for i in range(s):
    m=m+l4[i]
    avtat=m/s
print(avtat)
n=0
for i in range(s):
    n=n+l5[i]
    avwit=n/s
print(avwit)