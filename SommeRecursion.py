def sommeElement(arr,n):
    n=len(arr)
    if n==0 :
        return 0
    else:
        return sommeElement(arr,n-1)+arr(n-1)




file = open('/home/dyhia/Documents/arithm/data1/TD7-File1-N100-C10e3.txt', encoding='utf8')
# read = file.read()
# file.seek(0)
# read

# print(read)
#print

arr=[]
n=len(arr)
# N=len(arr)
# print(N)
for x in file:
#   print(x)
    arr.append(x)
# print(arr)

values = map(float, arr)

values = []
for s in arr:
     values.append(float(s))

print("array avant le tri est:")
print("\n\n")
for i in arr:
	print(i, end = ' ')


resultatSomme=sommeElement(values,n)
print(resultatSomme)
