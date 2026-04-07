print('This program calculate the sum of the series s= 1+x+x**2+x**3....+x**n ')
print('Click Enter to proceed ')
input('>>>')
x=int(input('Enter the value of x ==> '))
n=int(input('Enter the value of n ==> '))
sum=0
for i in range(n+1):
    sum+=x**i
print(f'sum of the series is {sum}')
