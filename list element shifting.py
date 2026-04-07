a=[10,23,25,56,12,34]
print(a)
print('This program shifts the elements of the list to the next place. ')
n=len(a)
l=a[-1]
for i in range(n-1,0,-1):
    a[i]=a[i-1]
a[0]=l
print(f'After the shifting the list is {a}')